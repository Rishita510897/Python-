import re

SKILLS_DB = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "statistics", "aws", "git", "streamlit",
    "project management", "communication"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS_DB:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.append(skill)

    return found

def assign_confidence(skills):
    return {skill: 70 + (i % 20) for i, skill in enumerate(skills)}
