import matplotlib.pyplot as plt

def plot_similarity_bubble_matrix(sim_df):
    fig, ax = plt.subplots(figsize=(10, 6))

    resume_skills = sim_df.index.tolist()
    jd_skills = sim_df.columns.tolist()

    for y, resume_skill in enumerate(resume_skills):
        for x, jd_skill in enumerate(jd_skills):
            score = sim_df.loc[resume_skill, jd_skill]

            # Determine color based on threshold
            if score >= 0.8:
                color = "#4CAF50"   # Green
            elif score >= 0.5:
                color = "#FFC107"   # Yellow
            else:
                color = "#F44336"   # Red

            # Bubble size (scaled)
            size = score * 1200

            ax.scatter(
                x, y,
                s=size,
                color=color,
                alpha=0.85
            )

    ax.set_xticks(range(len(jd_skills)))
    ax.set_yticks(range(len(resume_skills)))

    ax.set_xticklabels(jd_skills, rotation=30, ha="right")
    ax.set_yticklabels(resume_skills)

    ax.set_xlabel("Job Description Skills")
    ax.set_ylabel("Resume Skills")
    ax.set_title("Similarity Matrix")

    # Legend
    ax.scatter([], [], s=200, color="#4CAF50", label="High Match (80–100%)")
    ax.scatter([], [], s=200, color="#FFC107", label="Partial Match (50–79%)")
    ax.scatter([], [], s=200, color="#F44336", label="Low Match (0–49%)")

    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,
        frameon=False
    )

    ax.grid(True, linestyle="--", alpha=0.3)

    return fig
