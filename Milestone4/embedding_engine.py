from sentence_transformers import SentenceTransformer

_model_cache = {}

def embed_list(skills, model_name):
    if model_name not in _model_cache:
        _model_cache[model_name] = SentenceTransformer(model_name)

    model = _model_cache[model_name]
    return model.encode(skills, convert_to_tensor=True)
