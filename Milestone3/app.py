import streamlit as st
import numpy as np
import streamlit.components.v1 as components

from milestone2.skill_extractor import extract_skills
from skill_normalizer import clean_skill_list
from embedding_engine import embed_list
from similarity_engine import create_similarity_matrix, best_skill_matches
from report_generator import generate_skill_gap_report, save_report
from visualization import plot_similarity_bubble_matrix
from file_loader import load_file   # ✅ moved up

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(layout="wide")
st.title("Milestone 3: Skill Gap Analysis & Similarity Matching")

# ✅ DEFINE MODEL NAME (VERY IMPORTANT)
model_name = "all-MiniLM-L6-v2"

# -------------------------------
# FILE UPLOAD
# -------------------------------
st.subheader("📄 Upload Files")

resume_file = st.file_uploader(
    "Upload Resume (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

jd_file = st.file_uploader(
    "Upload Job Description (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

# -------------------------------
# MAIN LOGIC
# -------------------------------
if st.button("Run Skill Gap Analysis"):

    if resume_file is None or jd_file is None:
        st.error("Please upload both Resume and Job Description files.")
        st.stop()

    resume_text = load_file(resume_file)
    jd_text = load_file(jd_file)

    resume_skills = clean_skill_list(extract_skills(resume_text))
    jd_skills = clean_skill_list(extract_skills(jd_text))

    if not resume_skills or not jd_skills:
        st.error("No skills extracted. Please check the uploaded files.")
        st.stop()

    resume_embeddings = embed_list(resume_skills, model_name)
    jd_embeddings = embed_list(jd_skills, model_name)

    sim_df = create_similarity_matrix(
        resume_embeddings,
        jd_embeddings,
        resume_skills,
        jd_skills
    )

    best_matches = best_skill_matches(sim_df)
    alignment_score = np.mean([float(v["score"]) for v in best_matches.values()])

    report = generate_skill_gap_report(
        resume_skills,
        jd_skills,
        best_matches,
        alignment_score
    )

    save_report(report)

    # -------------------------------
    # RESULTS UI
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Similarity Matrix")
        st.pyplot(plot_similarity_bubble_matrix(sim_df))

    with col2:
        st.metric("Overall Match", f"{alignment_score*100:.2f}%")
        st.metric("Matched Skills", len(report["matched_skills"]))
        st.metric("Partial Matches", len(report["partial_skills"]))
        st.metric("Missing Skills", len(report["missing_skills"]))

    # -------------------------------
    # MISSING SKILLS UI
    # -------------------------------
    st.subheader("⚠️ Missing Skills")

    missing_skills = report["missing_skills"]

    if not missing_skills:
        st.success("No missing skills found 🎉")
    else:
        for skill in missing_skills:

            skill_name = (
                skill["job_skill"]
                if isinstance(skill, dict)
                else str(skill)
            )

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
                                {skill_name}
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
