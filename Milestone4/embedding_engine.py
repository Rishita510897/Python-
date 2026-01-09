import os
from sentence_transformers import SentenceTransformer

# Force single-threading to avoid Python 3.12 RuntimeError
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

_model_cache = {}

def embed_list(skills, model_name):
    if model_name not in _model_cache:
        _model_cache[model_name] = SentenceTransformer(model_name)

    model = _model_cache[model_name]

    # Encode embeddings safely
    return model.encode(
        skills,
        convert_to_tensor=True,
        show_progress_bar=False,  # Disable tqdm
        batch_size=16,            # Smaller batch size is safer
        device='cpu'              # Optional: force CPU to avoid thread issues
    )
