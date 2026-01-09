ABBREVIATIONS = {
    "ml": "machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing"
}

def normalize_skill(skill: str) -> str:
    if not skill:
        return ""
    skill = skill.lower().strip()
    return ABBREVIATIONS.get(skill, skill)

def clean_skill_list(skills):
    cleaned = set()
    for skill in skills:
        norm = normalize_skill(skill)
        if norm:
            cleaned.add(norm)
    return list(cleaned)
