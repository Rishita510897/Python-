import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
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
# =====================================================
# MILESTONE 3: SIMILARITY MATRIX + MISSING SKILLS (Safe Version)
# =====================================================

import os

# Force single-threading to prevent RuntimeError in Python 3.12
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

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
        # -------- EMBEDDINGS (Safe) --------
        from embedding_engine import embed_list

        model_name = "all-MiniLM-L6-v2"
        resume_emb = embed_list(
            st.session_state.resume_clean,
            model_name
        )
        jd_emb = embed_list(
            st.session_state.jd_clean,
            model_name
        )

        # -------- SIMILARITY MATRIX --------
        sim_df = create_similarity_matrix(
            resume_emb,
            jd_emb,
            st.session_state.resume_clean,
            st.session_state.jd_clean
        )

        # -------- BEST MATCHES --------
        best_matches = best_skill_matches(sim_df)

        # -------- CATEGORIZE MATCHED / PARTIAL / MISSING SKILLS --------
        matched, partial, missing_skills = 0, 0, []
        for jd_skill, data in best_matches.items():
            try:
                score = float(data["score"])
            except (ValueError, TypeError):
                score = 0

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

        # -------- SAVE SESSION STATE FOR MILESTONE 4 --------
        st.session_state.sim_df = sim_df
        st.session_state.best_matches = best_matches
        st.session_state.alignment_score = overall_match / 100
        st.session_state.m3_done = True


# =====================================================
# MILESTONE 4: CSV REPORT (Safe Version)
# =====================================================
if st.session_state.m3_done:
    st.markdown("---")
    st.subheader("📊 Milestone 4: Skill Gap Report")

    # -------------------------------
    # LOAD SESSION DATA SAFELY
    # -------------------------------
    overall_match = st.session_state.get("alignment_score", 0) * 100
    best_matches = st.session_state.get("best_matches", {})
    sim_df = st.session_state.get("sim_df", pd.DataFrame())
    resume_skills = st.session_state.get("resume_clean", [])
    jd_skills = st.session_state.get("jd_clean", [])

    # -------------------------------
    # Categorize skills
    # -------------------------------
    matched_skills = [v.get("resume_skill","") for v in best_matches.values() if float(v.get("score",0)) >= 0.8]
    partial_skills = [v.get("resume_skill","") for v in best_matches.values() if 0.5 <= float(v.get("score",0)) < 0.8]
    missing_skills = [k for k, v in best_matches.items() if float(v.get("score",0)) < 0.5]

    # -------------------------------
    # Skill Match Overview
    # -------------------------------
    st.subheader("Skill Match Overview")
    col1, col2, col3 = st.columns([1, 1, 1])
    col1.metric("Overall Match", f"{overall_match:.0f}%")
    col2.metric("Matched Skills", len(matched_skills))
    col3.metric("Missing Skills", len(missing_skills))

    # -------------------------------
    # Skill Comparison Bar Chart (Plotly)
    # -------------------------------
    if not sim_df.empty:
        avg_scores = sim_df.groupby("resume_skill")["similarity"].max().reset_index()
        avg_scores["similarity_pct"] = avg_scores["similarity"] * 100

        import plotly.express as px
        fig_bar = px.bar(
            avg_scores,
            x="resume_skill",
            y="similarity_pct",
            labels={"similarity_pct": "Match %", "resume_skill": "Skills"},
            text="similarity_pct",
            color="similarity_pct",
            color_continuous_scale=["red","orange","green"]
        )
        fig_bar.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

        # Progress bars (safe clamped)
        st.subheader("Skill Comparison")
        for _, row in avg_scores.iterrows():
            st.write(f"{row['resume_skill']}")
            pct = min(max(int(row["similarity_pct"]),0),100)
            st.progress(pct)

    # -------------------------------
    # Role View Radar Chart
    # -------------------------------
    st.subheader("Role View")
    import plotly.graph_objects as go
    categories = ["Technical Skills", "Soft Skills", "Experience", "Education", "Certifications"]
    resume_values = [overall_match] * len(categories)
    jd_values = [100] * len(categories)

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=resume_values,
        theta=categories,
        fill='toself',
        name='Current Profile',
        line_color='blue'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=jd_values,
        theta=categories,
        fill='toself',
        name='Job Requirements',
        line_color='green'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,100])),
        showlegend=True, height=400
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # -------------------------------
    # Upskilling Recommendations
    # -------------------------------
    st.subheader("Upskilling Recommendations")
    recommendations = []

    for skill in missing_skills:
        if "AWS" in skill.upper():
            recommendations.append(("AWS Cloud Services", "Complete AWS Certified Solutions Architect course"))
        elif "STAT" in skill.upper() or "SQL" in skill.upper():
            recommendations.append(("Advanced Statistics / SQL", "Enroll in Advanced Statistics or SQL for Data Science"))
        elif "PROJECT" in skill.upper() or "MGMT" in skill.upper():
            recommendations.append(("Project Management", "Consider PMP certification for leadership skills"))
        else:
            recommendations.append((skill, f"Improve your {skill} skill"))

    for title, desc in recommendations:
        st.markdown(f"**{title}** - {desc}")

    # -------------------------------
    # Create DataFrame for CSV export safely
    # -------------------------------
    if not sim_df.empty:
        df = pd.DataFrame([
            {
                "Resume Skill": v.get("resume_skill",""),
                "Job Skill": k,
                "Match %": round(float(v.get("score",0)) * 100, 2)
            }
            for k, v in best_matches.items()
        ])
    else:
        df = pd.DataFrame(columns=["Resume Skill", "Job Skill", "Match %"])
    # Download button
    st.download_button(
        "⬇️ Download Skill Gap Report (CSV)",
        df.to_csv(index=False),
        "skill_gap_report.csv",
        "text/csv"
    )

