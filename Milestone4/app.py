import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from file_loader import load_file
from milestone2.skill_extractor import extract_skills
from skill_normalizer import clean_skill_list
from embedding_engine import embed_list
from similarity_engine import create_similarity_matrix, best_skill_matches
from report_generator import generate_skill_gap_report
from visualization import plot_similarity_bubble_matrix

st.set_page_config(layout="wide")
st.title("Skill Gap Analyzer (Milestone-wise View)")
def parse_resume(file):
    import re
    import docx
    import PyPDF2

    text = ""
    if file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])

    name = re.search(r"Name[:\s]+([A-Za-z ]+)", text)
    email = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.search(r"\+?\d[\d\s-]{8,}\d", text)
    skills = re.findall(r"\b([A-Za-z+#]+)\b", text)

    return {
        "name": name.group(1).strip() if name else "",
        "email": email.group(0) if email else "",
        "phone": phone.group(0) if phone else "",
        "skills": skills
    }

# -------------------------------
# SESSION STATE INIT
# -------------------------------
for key in [
    "resume_text", "jd_text",
    "resume_data", "jd_data",
    "m1_done", "m2_done", "m3_done"
]:
    if key not in st.session_state:
        st.session_state[key] = False

# -------------------------------
# FILE UPLOAD (ONLY INPUTS)
# -------------------------------
st.subheader("📄 Upload Files")
resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

if resume_file and jd_file:
    # -----------------------
    # LOAD TEXT
    # -----------------------
    resume_text = load_file(resume_file)
    jd_text = load_file(jd_file)

    # -----------------------
    # PARSE STRUCTURED DATA
    # -----------------------
    resume_data = parse_resume(resume_file)  # returns dict with name, email, phone, skills
    jd_data = parse_resume(jd_file)  # returns dict with title, skills, etc.

    # Save to session state
    st.session_state.resume_text = resume_text
    st.session_state.jd_text = jd_text
    st.session_state.resume_data = resume_data
    st.session_state.jd_data = jd_data
    st.session_state.m1_done = True

# =====================================================
# MILESTONE 1: SHOW STRUCTURED DATA + EXTRACT SKILLS
# =====================================================
if st.session_state.m1_done:
    st.markdown("---")
    st.subheader("✅ Milestone 1: Extracted Data and Skills")

    # ----------------- Resume -----------------
    st.markdown("**Resume Data (Parsed from file)**")
    st.json({
        "Name": st.session_state.resume_data.get("name", ""),
        "Email": st.session_state.resume_data.get("email", ""),
        "Phone": st.session_state.resume_data.get("phone", ""),
        "Raw Skills": st.session_state.resume_data.get("skills", [])
    })

    # Extract skills from resume text
    resume_skills = extract_skills(st.session_state.resume_text)
    st.write("**Extracted Skills from Resume Text:**", resume_skills)

    # ----------------- Job Description -----------------
    st.markdown("**Job Description Data (Parsed from file)**")
    st.json({
        "Title / Role": st.session_state.jd_data.get("title", ""),
        "Required Skills": st.session_state.jd_data.get("skills", [])
    })

    # Extract skills from JD text
    jd_skills = extract_skills(st.session_state.jd_text)
    st.write("**Extracted Skills from JD Text:**", jd_skills)

    # Save skills for next milestone
    st.session_state.resume_skills = resume_skills
    st.session_state.jd_skills = jd_skills
    st.session_state.m2_done = True

# =====================================================
# MILESTONE 2: SKILL CLEANING & NORMALIZATION
# =====================================================
if st.session_state.m2_done:
    st.markdown("---")
    st.subheader("🧹 Milestone 2: Clean & Normalize Skills")

    resume_clean = clean_skill_list(st.session_state.resume_skills)
    jd_clean = clean_skill_list(st.session_state.jd_skills)

    st.write("**Cleaned Resume Skills:**", resume_clean)
    st.write("**Cleaned JD Skills:**", jd_clean)

    st.session_state.resume_clean = resume_clean
    st.session_state.jd_clean = jd_clean
    st.session_state.m3_done = True

# =====================================================
# MILESTONE 3: SIMILARITY MATCHING
# =====================================================
# =====================================================
# MILESTONE 3: SKILL GAP & SIMILARITY MATCHING (MODIFIED)
# =====================================================
import streamlit.components.v1 as components

if st.session_state.m3_done:
    st.markdown("---")
    st.subheader("🔍 Milestone 3: Skill Gap Analysis & Similarity Matching")

    # ------------------ EMBEDDINGS ------------------
    model_name = "all-MiniLM-L6-v2"

    resume_emb = embed_list(st.session_state.resume_clean, model_name)
    jd_emb = embed_list(st.session_state.jd_clean, model_name)

    # ------------------ SIMILARITY MATRIX ------------------
    sim_df = create_similarity_matrix(
        resume_emb,
        jd_emb,
        st.session_state.resume_clean,
        st.session_state.jd_clean
    )

    best_matches = best_skill_matches(sim_df)

    # ------------------ MATCH COUNTS ------------------
    matched = 0
    partial = 0
    missing_skills = []

    for jd_skill, data in best_matches.items():
        score = float(data.get("score", 0))

        if score >= 0.80:
            matched += 1
        elif score >= 0.50:
            partial += 1
        else:
            missing_skills.append(jd_skill)

    # ------------------ OVERALL MATCH ------------------
    overall_match = (
        (matched + (0.5 * partial)) / len(st.session_state.jd_clean)
    ) * 100

    # ------------------ METRICS ------------------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Overall Match", f"{overall_match:.2f}%")
    col2.metric("Matched Skills", matched)
    col3.metric("Partial Matches", partial)
    col4.metric("Missing Skills", len(missing_skills))

    # ------------------ VISUALIZATION ------------------
    st.pyplot(plot_similarity_bubble_matrix(sim_df))

    # ------------------ MISSING SKILLS UI ------------------
    st.subheader("⚠ Missing Skills")

    if not missing_skills:
        st.success("No missing skills found 🎉")
    else:
        for skill in missing_skills:
            components.html(
                f"""
                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    padding:14px 16px;
                    margin-bottom:12px;
                    border-radius:14px;
                    background-color:#F8F9FA;
                    border:1px solid #E0E0E0;
                ">
                    <div style="display:flex;align-items:center;">
                        <div style="
                            background-color:#6F42C1;
                            color:white;
                            width:38px;
                            height:38px;
                            border-radius:50%;
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            margin-right:12px;
                            font-size:18px;">
                            ⚠️
                        </div>
                        <div>
                            <div style="font-weight:600;">
                                {skill}
                            </div>
                            <div style="font-size:12px;color:#6C757D;">
                                Technical Skill
                            </div>
                        </div>
                    </div>

                    <span style="
                        background-color:#FDECEA;
                        color:#D32F2F;
                        padding:6px 12px;
                        border-radius:14px;
                        font-size:12px;
                        font-weight:600;
                    ">
                        High
                    </span>
                </div>
                """,
                height=90
            )

    # ------------------ SAVE FOR MILESTONE 4 ------------------
    st.session_state.sim_df = sim_df
    st.session_state.best_matches = best_matches
    st.session_state.alignment_score = overall_match / 100



# =====================================================
# MILESTONE 4: REPORT + CSV DOWNLOAD
# =====================================================
if st.session_state.m3_done:
    st.markdown("---")
    st.subheader("📊 Milestone 4: Skill Gap Report")

    report = generate_skill_gap_report(
        st.session_state.resume_clean,
        st.session_state.jd_clean,
        st.session_state.best_matches,
        st.session_state.alignment_score
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Matched Skills", len(report.get("matched_skills", [])))
    col2.metric("Partial Skills", len(report.get("partial_skills", [])))
    col3.metric("Missing Skills", len(report.get("missing_skills", [])))

    # CSV DOWNLOAD
    df = pd.DataFrame([
        {
            "Job Skill": k,
            "Resume Skill": v.get("resume_skill", ""),
            "Similarity Score": v.get("score", 0)
        }
        for k, v in st.session_state.best_matches.items()
    ])

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Skill Gap Report (CSV)",
        csv,
        "skill_gap_report.csv",
        "text/csv"
    )
