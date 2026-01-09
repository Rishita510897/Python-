import matplotlib.pyplot as plt
import numpy as np

def plot_similarity_bubble_matrix(sim_df):
    """
    sim_df: pandas DataFrame with resume skills as rows, JD skills as columns,
            values are similarity scores (0-1)
    """
    resume_skills = sim_df.index.tolist()
    jd_skills = sim_df.columns.tolist()

    # Convert DataFrame to arrays for plotting
    x, y, sizes, colors = [], [], [], []

    for i, resume in enumerate(resume_skills):
        for j, jd in enumerate(jd_skills):
            score = sim_df.loc[resume, jd]
            x.append(j)
            y.append(i)
            sizes.append(score * 1000)  # scale bubble size
            # color based on thresholds
            if score >= 0.8:
                colors.append("green")    # High match
            elif score >= 0.5:
                colors.append("gold")     # Partial match
            else:
                colors.append("red")      # Low match

    fig, ax = plt.subplots(figsize=(len(jd_skills)*1.2, len(resume_skills)*0.8))

    scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, edgecolors="w")

    # Set axis labels
    ax.set_xticks(range(len(jd_skills)))
    ax.set_xticklabels(jd_skills, rotation=45, ha="right", fontsize=10)
    ax.set_yticks(range(len(resume_skills)))
    ax.set_yticklabels(resume_skills, fontsize=10)

    # Set title
    ax.set_title("Similarity Matrix", fontsize=14, pad=15)

    # Create legend manually
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='High Match (80-100%)',
               markerfacecolor='green', markersize=12),
        Line2D([0], [0], marker='o', color='w', label='Partial Match (50-79%)',
               markerfacecolor='gold', markersize=12),
        Line2D([0], [0], marker='o', color='w', label='Low Match (0-49%)',
               markerfacecolor='red', markersize=12)
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))

    ax.invert_yaxis()  # so first resume skill is at top
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    return fig
