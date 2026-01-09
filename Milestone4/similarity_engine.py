import pandas as pd
import torch
import torch.nn.functional as F

def create_similarity_matrix(resume_emb, jd_emb, resume_skills, jd_skills):
    """
    Creates cosine similarity matrix between resume skills and job skills
    """

    # Normalize embeddings
    resume_norm = F.normalize(resume_emb, p=2, dim=1)
    jd_norm = F.normalize(jd_emb, p=2, dim=1)

    # Cosine similarity matrix
    sim_matrix = torch.matmul(resume_norm, jd_norm.T)

    return pd.DataFrame(
        sim_matrix.cpu().numpy(),
        index=resume_skills,
        columns=jd_skills
    )


def best_skill_matches(sim_df, threshold=0.7):
    """
    Finds best matching job skill for each resume skill
    """
    results = {}

    for r_skill in sim_df.index:
        best_j = sim_df.loc[r_skill].idxmax()
        best_score = sim_df.loc[r_skill].max()

        results[r_skill] = {
            "job_skill": best_j,
            "score": float(best_score),
            "match": best_score >= threshold
        }

    return results
