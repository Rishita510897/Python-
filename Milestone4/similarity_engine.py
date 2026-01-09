import torch
import torch.nn.functional as F
import pandas as pd

def create_similarity_matrix(resume_emb, jd_emb, resume_skills, jd_skills):

    # ✅ Convert to tensor if needed
    resume_emb = torch.tensor(resume_emb) if not torch.is_tensor(resume_emb) else resume_emb
    jd_emb = torch.tensor(jd_emb) if not torch.is_tensor(jd_emb) else jd_emb

    # ✅ FIX: ensure 2D
    if resume_emb.dim() == 1:
        resume_emb = resume_emb.unsqueeze(0)

    if jd_emb.dim() == 1:
        jd_emb = jd_emb.unsqueeze(0)

    # ✅ Normalize
    resume_norm = F.normalize(resume_emb, p=2, dim=1)
    jd_norm = F.normalize(jd_emb, p=2, dim=1)

    # ✅ Cosine similarity
    similarity = torch.mm(resume_norm, jd_norm.T)

    # ✅ Build DataFrame
    rows = []
    for i, r_skill in enumerate(resume_skills):
        for j, j_skill in enumerate(jd_skills):
            rows.append({
                "resume_skill": r_skill,
                "jd_skill": j_skill,
                "resume_index": i,
                "jd_index": j,
                "similarity": float(similarity[i][j])
            })

    return pd.DataFrame(rows)
def best_skill_matches(sim_df):
    """
    For each JD skill, find the best matching resume skill
    based on highest similarity score.
    """

    best_matches = {}

    for jd_skill in sim_df["jd_skill"].unique():
        subset = sim_df[sim_df["jd_skill"] == jd_skill]

        best_row = subset.loc[subset["similarity"].idxmax()]

        best_matches[jd_skill] = {
            "resume_skill": best_row["resume_skill"],
            "score": float(best_row["similarity"])
        }

    return best_matches

