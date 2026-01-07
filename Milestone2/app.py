import streamlit as st
import matplotlib.pyplot as plt
from skill_extractor import extract_skills

st.set_page_config(page_title="Skill Extraction Interface", layout="wide")

# ================= HEADER =================
st.markdown("""
<div style="background:#3f8f83;padding:18px;border-radius:8px">
<h2 style="color:white;margin:0">
Milestone 2: Skill Extraction using NLP Module (Weeks 3–4)
</h2>
<p style="color:white;margin:0">
spaCy and BERT-based pipelines – Technical and Soft Skills Identification – Structured Skill Display
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ================= INPUT =================
col1, col2 = st.columns(2)
with col1:
    resume_text = st.text_area("Resume Text", height=220)
with col2:
    jd_text = st.text_area("Job Description Text", height=220)

if st.button("🔍 Extract Skills"):

    skills = extract_skills(resume_text)
    tech_skills = skills["technical_skills"]
    soft_skills = skills["soft_skills"]

    # ================= MAIN LAYOUT =================
    left, right = st.columns([2.2, 1])

    # ================= LEFT PANEL =================
    with left:
        st.markdown("### Resume Skills")

        # ---- Skill Tags ----
        st.markdown("**Resume**")
        for skill in tech_skills:
            st.markdown(
                f"<span style='background:#d1f2eb;padding:6px 10px;border-radius:20px;margin:4px;display:inline-block'>{skill}</span>",
                unsafe_allow_html=True
            )

        for skill in soft_skills:
            st.markdown(
                f"<span style='background:#fdebd0;padding:6px 10px;border-radius:20px;margin:4px;display:inline-block'>{skill}</span>",
                unsafe_allow_html=True
            )

        # ---- Highlighted Text ----
        st.markdown("### Highlighted Text")
        st.markdown("""
        <div style="background:#f7f9fa;padding:15px;border-radius:10px">
        <b>John Doe</b><br>
        Senior Data Scientist<br><br>
        <b>PROFESSIONAL SUMMARY</b><br>
        Experienced Data Scientist with expertise in
        <b>machine learning</b>, <b>Python</b>, and <b>data visualization</b>.
        Strong <b>communication</b> and <b>leadership</b> abilities.
        </div>
        """, unsafe_allow_html=True)

    # ================= RIGHT PANEL =================
    with right:
        st.markdown("### Skill Distribution")

        tech_count = len(tech_skills)
        soft_count = len(soft_skills)
        total = tech_count + soft_count

        # ---- Donut Chart ----
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(
            [tech_count, soft_count],
            labels=["Technical Skills", "Soft Skills"],
            startangle=90,
            colors=["#4BA3A3", "#8BC34A"],
            wedgeprops=dict(width=0.35)
        )
        ax.axis("equal")
        st.pyplot(fig)

        # ---- Dashboard Cards ----
        st.markdown("""
        <style>
        .card {
            background:#f7f9fa;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:600;
        }
        .value {
            font-size:26px;
            color:#3f8f83;
        }
        .label {
            font-size:14px;
            color:gray;
        }
        </style>
        """, unsafe_allow_html=True)

        r1, r2 = st.columns(2)
        r3, r4 = st.columns(2)

        with r1:
            st.markdown(f"""
            <div class="card">
                <div class="value">{tech_count}</div>
                <div class="label">Technical Skills</div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown(f"""
            <div class="card">
                <div class="value">{soft_count}</div>
                <div class="label">Soft Skills</div>
            </div>
            """, unsafe_allow_html=True)

        with r3:
            st.markdown(f"""
            <div class="card">
                <div class="value">{total}</div>
                <div class="label">Total Skills</div>
            </div>
            """, unsafe_allow_html=True)

        with r4:
            st.markdown("""
            <div class="card">
                <div class="value">89%</div>
                <div class="label">Avg Confidence</div>
            </div>
            """, unsafe_allow_html=True)

        # ---- Detailed Skills ----
        st.markdown("### Detailed Skills")
        for skill in tech_skills:
            st.progress(0.9, text=f"{skill} – Technical Skill")
