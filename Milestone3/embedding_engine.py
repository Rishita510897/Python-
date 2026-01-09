from sentence_transformers import SentenceTransformer
from functools import lru_cache

@lru_cache(maxsize=2)
def load_model(model_name: str):
    return SentenceTransformer(model_name)

@lru_cache(maxsize=1024)
def embed_single(skill: str, model_name: str):
    model = load_model(model_name)
    return model.encode(skill)

def embed_list(skills: list, model_name: str):
    model = load_model(model_name)
    return model.encode(skills)
