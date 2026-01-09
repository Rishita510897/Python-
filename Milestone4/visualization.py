# visualization.py
import matplotlib.pyplot as plt
import numpy as np

def plot_similarity_bubble_matrix(sim_df):
    """
    Plots a bubble chart of skill similarity between resume and job description skills.
    Bubbles are colored based on similarity:
        - Green: >= 0.8
        - Orange: 0.5 - 0.8
        - Red: < 0.5
    Bubble size is proportional to similarity score.
    """

    # Ensure similarity column is float
    sim_df["similarity"] = sim_df["similarity"].astype(float)

    fig, ax = plt.subplots(figsize=(10, 8))

    # Get unique skill labels for axis ticks
    resume_skills = list(sim_df["resume_skill"].unique())
    jd_skills = list(sim_df["jd_skill"].unique())

    # Plot each bubble
    for _, row in sim_df.iterrows():
        try:
            score = float(row["similarity"])
        except (ValueError, TypeError):
            score = 0  # fallback if invalid

        # Determine bubble color
        if score >= 0.8:
            color = "green"
        elif score >= 0.5:
            color = "orange"
        else:
            color = "red"

        ax.scatter(
            resume_skills.index(row["resume_skill"]),
            jd_skills.index(row["jd_skill"]),
            s=score * 500,  # bubble size proportional to similarity
            c=color,
            alpha=0.6,
            edgecolors="w"
        )

    # Set axis labels and ticks
    ax.set_xticks(range(len(resume_skills)))
    ax.set_xticklabels(resume_skills, rotation=45, ha="right")
    ax.set_yticks(range(len(jd_skills)))
    ax.set_yticklabels(jd_skills)
    ax.set_xlabel("Resume Skills")
    ax.set_ylabel("Job Description Skills")
    ax.set_title("📊 Skill Similarity Bubble Matrix")

    fig.tight_layout()
    return fig
