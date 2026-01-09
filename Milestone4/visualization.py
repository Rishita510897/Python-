import matplotlib.pyplot as plt

def plot_similarity_bubble_matrix(sim_df):
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, row in sim_df.iterrows():
        ax.scatter(
            row["resume_index"],
            row["jd_index"],
            s=row["similarity"] * 1000,
            alpha=0.6
        )

    ax.set_xlabel("Resume Skills")
    ax.set_ylabel("Job Description Skills")
    ax.set_title("Skill Similarity Matrix")

    return fig   
