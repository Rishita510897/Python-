import streamlit as st
import matplotlib.pyplot as plt
from skill_extractor import extract_skills, assign_confidence

st.set_page_config("Skill Extraction Interface", layout="wide")

# ---------------- HEADER ---------------- #
st.markdown("## Skill Extraction Interface")

left, right = st.columns([1.3, 1])

# ---------------- INPUT ---------------- #
with left:
    option = st.radio("Resume Skills", ["Resume", "Job Description"])
    text = st.text_area("", height=280)

if st.button("Extract Skills"):
    tech, soft = extract_skills(text)
    all_skills = list(dict.fromkeys(tech + soft))
    main_skills = all_skills[:8]

    confidence = assign_confidence(main_skills)

    total = len(all_skills)
    avg_conf = sum(confidence.values()) / len(confidence)

    # ---------------- LEFT PANEL ---------------- #
    with left:
        st.markdown("### Resume Skills")

        # Skill tags (SIDE BY SIDE)
        st.markdown("<div style='display:flex;flex-wrap:wrap'>", unsafe_allow_html=True)
        for skill, conf in confidence.items():
            st.markdown(
                f"""
                <span style="
                background:#e8f5f0;
                padding:6px 14px;
                border-radius:18px;
                margin:6px;
                font-size:13px;">
                {skill.title()} {conf}%
                </span>
                """,
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### Highlighted Text")
        st.write(text)

    # ---------------- RIGHT PANEL ---------------- #
    with right:
        st.markdown("### Skill Distribution")

        fig, ax = plt.subplots()
        ax.pie(
            [len(tech), len(soft)],
            labels=["Technical Skills", "Soft Skills"],
            autopct="%1.0f%%",
            startangle=90
        )
        ax.axis("equal")
        st.pyplot(fig)

        # STATS
        col1, col2 = st.columns(2)
        col1.metric("Technical Skills", len(tech))
        col1.metric("Soft Skills", len(soft))
        col2.metric("Total Skills", total)
        col2.metric("Avg Confidence", f"{avg_conf:.0f}%")

        # ---------------- DETAILED SKILLS ---------------- #
        st.markdown("### Detailed Skills")
        for skill, conf in confidence.items():
            st.markdown(f"**{skill.title()}**")
            st.progress(conf / 100)
