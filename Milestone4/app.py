import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Milestone 2 skill extractor
from milestone2.skill_extractor import extract_skills, assign_confidence

# Other modules
from file_loader import load_file
from skill_normalizer import clean_skill_list
from embedding_engine import embed_list
from similarity_engine import create_similarity_matrix, best_skill_matches
from report_generator import generate_skill_gap_report
from visualization import plot_similarity_bubble_matrix

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")
st.title("Skill Gap Analyzer (Milestone-wise View)")

# ---------------- SESSION STATE ----------------
defaults = {
    "resume_text": "",
    "jd_text": "",
    "resume_skills": [],
    "jd_skills": [],
    "resume_clean": [],
    "jd_clean": [],
    "best_matches": {},
    "sim_df": None,
    "alignment_score": 0.0,
    "m1_done": False,
    "m2_done": False,
    "m3_done": False
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------------- FILE UPLOAD ----------------
st.subheader("📄 Upload Files")
resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

if resume_file and jd_file:
    st.session_state.resume_text = load_file(resume_file)
    st.session_state.jd_text = load_file(jd_file)
    st.session_state.m1_done = True

# =====================================================
# MILESTONE 1: Document Upload & Preview
# =====================================================
if st.session_state.m1_done:
    st.markdown("---")
    st.subheader("✅ Milestone 1: Document Upload & Parsing")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📄 Resume Preview")
        st.text_area("Resume", value=st.session_state.resume_text, height=300)
    with col2:
        st.markdown("### 📑 Job Description Preview")
        st.text_area("Job Description", value=st.session_state.jd_text, height=300)

    # Move to Milestone 2
    st.session_state.m2_done = True

# =====================================================
# MILESTONE 2: Skill Cleaning & Normalization
# =====================================================
if st.session_state.m2_done:
    st.markdown("---")
    st.subheader("🧹 Milestone 2: Skill Cleaning & Normalization")

    # Extract resume skills automatically
    resume_text = st.session_state.get("resume_text", "")
    if resume_text and not st.session_state.get("resume_skills"):
        resume_tech, resume_soft = extract_skills(resume_text)
        st.session_state.resume_skills = resume_tech + resume_soft

    resume_skills = st.session_state.get("resume_skills", [])
    jd_skills = st.session_state.get("jd_skills", [])

    # Clean skills
    resume_clean = clean_skill_list(resume_skills)
    jd_clean = clean_skill_list(jd_skills)
    st.session_state.resume_clean = resume_clean
    st.session_state.jd_clean = jd_clean

    # Assign confidence
    confidence_map = assign_confidence(resume_clean) if resume_clean else {}
    avg_conf = sum(confidence_map.values()) / len(confidence_map) if confidence_map else 0
    tech_count = len(resume_clean)
    soft_count = 0
    total_count = tech_count + soft_count

    # Layout
    left, right = st.columns([1.3, 1])
    with left:
        st.markdown("### 📄 Resume Skills")
        if confidence_map:
            for skill, score in confidence_map.items():
                st.markdown(
                    f"<span style='background:#E6F4F1;padding:6px 12px;border-radius:16px;margin:4px;display:inline-block;'>"
                    f"{skill.title()} <b>{score}%</b></span>",
                    unsafe_allow_html=True
                )
        st.markdown("### ✨ Highlighted Text")
        st.text_area("Resume Text", resume_text, height=220)

    with right:
        st.markdown("### 📊 Skill Distribution")
        st.metric("Technical Skills", tech_count)
        st.metric("Soft Skills", soft_count)
        st.metric("Total Skills", total_count)
        st.metric("Avg. Confidence", f"{avg_conf:.0f}%")

        fig, ax = plt.subplots()
        pie_values = [tech_count, soft_count] if (tech_count + soft_count) > 0 else [1, 1]
        ax.pie(pie_values, labels=["Technical", "Soft"], autopct=lambda p: f"{p:.0f}%", startangle=90,
               colors=["#1f77b4", "#ff7f0e"])
        ax.axis("equal")
        st.pyplot(fig)

    st.markdown("### 📋 Detailed Skills")
    if confidence_map:
        for skill, score in confidence_map.items():
            st.markdown(f"**{skill.title()}**")
            st.progress(score / 100)
    else:
        st.write("No detailed skills to display.")

    # Move to Milestone 3
    st.session_state.m3_done = True


# =====================================================
# MILESTONE 3: SIMILARITY MATRIX + MISSING SKILLS
# =====================================================
if st.session_state.m2_done:
    st.markdown("---")
    st.subheader("🔍 Milestone 3: Skill Gap & Similarity Matching")

    # --------- AUTO-EXTRACT JD SKILLS IF EMPTY ---------
    if st.session_state.jd_text and not st.session_state.jd_skills:
        jd_tech, jd_soft = extract_skills(st.session_state.jd_text)
        st.session_state.jd_skills = jd_tech + jd_soft
        st.session_state.jd_clean = clean_skill_list(st.session_state.jd_skills)

    # Check if both resume and JD have skills
    if not st.session_state.resume_clean:
        st.warning("No skills detected in the resume. Cannot compute similarity.")
    elif not st.session_state.jd_clean:
        st.warning("No skills detected in the Job Description. Cannot compute similarity.")
    else:
        # -------- EMBEDDINGS --------
        model_name = "all-MiniLM-L6-v2"
        resume_emb = embed_list(st.session_state.resume_clean, model_name)
        jd_emb = embed_list(st.session_state.jd_clean, model_name)

        # -------- SIMILARITY MATRIX --------
        sim_df = create_similarity_matrix(
            resume_emb,
            jd_emb,
            st.session_state.resume_clean,
            st.session_state.jd_clean
        )

        # -------- BEST MATCHES --------
        best_matches = best_skill_matches(sim_df)

        # Categorize matched / partial / missing skills
        matched, partial, missing_skills = 0, 0, []
        for jd_skill, data in best_matches.items():
            try:
                score = float(data["score"])  # <-- ensure score is a float
            except (ValueError, TypeError):
                score = 0  # fallback if conversion fails

            if score >= 0.8:
                matched += 1
            elif score >= 0.5:
                partial += 1
            else:
                missing_skills.append(jd_skill)

        overall_match = ((matched + 0.5 * partial) / len(st.session_state.jd_clean)) * 100

        # -------- METRICS --------
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Overall Match", f"{overall_match:.2f}%")
        c2.metric("Matched Skills", matched)
        c3.metric("Partial Matches", partial)
        c4.metric("Missing Skills", len(missing_skills))

        # -------- BUBBLE CHART --------
        st.subheader("📊 Skill Similarity Matrix")
        st.pyplot(plot_similarity_bubble_matrix(sim_df))

        # -------- MISSING SKILLS DISPLAY --------
        st.subheader("⚠ Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                components.html(f"""
                    <div style="padding:14px;margin-bottom:10px;border-radius:12px;
                    background:#FDECEA;border:1px solid #F5C6CB;">
                    ⚠️ <b>{skill}</b>
                    </div>
                """, height=70)
        else:
            st.success("No missing skills 🎉")

        # Save session state for Milestone 4
        st.session_state.sim_df = sim_df
        st.session_state.best_matches = best_matches
        st.session_state.alignment_score = overall_match / 100
        st.session_state.m3_done = True

# =====================================================
# MILESTONE 4: CSV REPORT
# =====================================================

if st.session_state.m3_done:
    st.markdown("---")
    st.subheader("📊 Milestone 4: Skill Gap Report")

    df = pd.DataFrame([
        {
            "Job Skill": k,
            "Resume Skill": v["resume_skill"],
            "Similarity Score": round(v["score"], 2)
        }
        for k, v in st.session_state.best_matches.items()
    ])

    # Display table
    st.dataframe(df)

    # Download button
    st.download_button(
        "⬇️ Download Skill Gap Report (CSV)",
        df.to_csv(index=False),
        "skill_gap_report.csv",
        "text/csv"
    )