import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from file_loader import load_file
from milestone2.skill_extractor import extract_skills
from skill_normalizer import clean_skill_list
from embedding_engine import embed_list
from similarity_engine import create_similarity_matrix, best_skill_matches
from report_generator import generate_skill_gap_report
from visualization import plot_similarity_bubble_matrix

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Skill Gap Analysis Dashboard", layout="wide")
st.title("📊 Skill Gap Analysis Dashboard")

MODEL_NAME = "all-MiniLM-L6-v2"

# ---------------- ROLE VIEW ----------------
st.subheader("👤 Role View")
role = st.radio("", ["Job Seeker", "Recruiter"], horizontal=True)

# ---------------- FILE UPLOAD ----------------
st.subheader("📄 Upload Files")
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume (PDF / DOCX / TXT)",
        type=["pdf", "docx", "txt"]
    )

with col2:
    jd_file = st.file_uploader(
        "Upload Job Description (PDF / DOCX / TXT)",
        type=["pdf", "docx", "txt"]
    )

# ---------------- ANALYSIS ----------------
if st.button("🔍 Analyze Skills"):

    if resume_file is None or jd_file is None:
        st.error("Please upload both Resume and Job Description files.")
        st.stop()

    # Load text (Milestone 1)
    resume_text = load_file(resume_file)
    jd_text = load_file(jd_file)

    # Skill extraction (Milestone 2)
    resume_skills = clean_skill_list(extract_skills(resume_text))
    jd_skills = clean_skill_list(extract_skills(jd_text))

    if not resume_skills or not jd_skills:
        st.error("No skills extracted. Please check input files.")
        st.stop()

    # Embeddings & similarity (Milestone 3)
    resume_emb = embed_list(resume_skills, MODEL_NAME)
    jd_emb = embed_list(jd_skills, MODEL_NAME)

    sim_df = create_similarity_matrix(
        resume_emb,
        jd_emb,
        resume_skills,
        jd_skills
    )

    matches = best_skill_matches(sim_df)
    alignment_score = np.mean([v["score"] for v in matches.values()])

    report = generate_skill_gap_report(
        resume_skills,
        jd_skills,
        matches,
        alignment_score
    )

    # ---------------- KPI CARDS ----------------
    st.subheader("📌 Skill Match Overview")
    k1, k2, k3 = st.columns(3)

    k1.metric("Overall Match", f"{report['overall_score']}%")
    k2.metric("Matched Skills", len(report["matched_skills"]))
    k3.metric("Missing Skills", len(report["missing_skills"]))

    # ---------------- VISUALS ----------------
    colA, colB = st.columns(2)

    with colA:
        st.subheader("📈 Skill Similarity Matrix")
        st.pyplot(plot_similarity_bubble_matrix(sim_df))

    with colB:
        st.subheader("📊 Skill Comparison")

        matched = report["matched_skills"]
        missing = report["missing_skills"]

        fig, ax = plt.subplots()
        ax.bar(matched, [1] * len(matched), label="Matched")
        ax.bar(missing, [0.4] * len(missing), label="Missing")
        ax.set_ylabel("Skill Coverage")
        ax.legend()
        st.pyplot(fig)

    # ---------------- UPSKILLING ----------------
    st.subheader("📚 Upskilling Recommendations")

    if not report["missing_skills"]:
        st.success("Great! No missing skills 🎉")
    else:
        for skill in report["missing_skills"]:
            st.info(
                f"🔹 **{skill.title()}** – Recommended: Online certification / hands-on project"
            )

    # ---------------- ROLE MESSAGE ----------------
    if role == "Recruiter":
        st.success("Recruiter View: Candidate skill alignment evaluated successfully.")
    else:
        st.info("Job Seeker View: Focus on missing skills to improve match score.")

