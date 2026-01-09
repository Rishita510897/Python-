import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]

def create_similarity_matrix(resume_embeddings, jd_embeddings, resume_skills, jd_skills):
    sim_matrix = cosine_similarity(resume_embeddings, jd_embeddings)
    return pd.DataFrame(sim_matrix, index=resume_skills, columns=jd_skills)

def best_skill_matches(sim_df):
    result = {}
    for jd_skill in sim_df.columns:
        scores = sim_df[jd_skill].sort_values(ascending=False)
        result[jd_skill] = {
            "best_resume_skill": scores.index[0],
            "score": scores.iloc[0],
            "top_3": scores.head(3).to_dict()
        }
    return result
