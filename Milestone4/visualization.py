import matplotlib.pyplot as plt

def plot_similarity_bubble_matrix(sim_df):
    fig, ax = plt.subplots(figsize=(8, 5))

    for i, r in enumerate(sim_df.index):
        for j, c in enumerate(sim_df.columns):
            ax.scatter(j, i, s=sim_df.loc[r, c]*600, alpha=0.6)

    ax.set_xticks(range(len(sim_df.columns)))
    ax.set_yticks(range(len(sim_df.index)))
    ax.set_xticklabels(sim_df.columns, rotation=45, ha="right")
    ax.set_yticklabels(sim_df.index)

    ax.set_title("Skill Similarity Matrix")
    return fig
