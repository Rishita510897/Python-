# skill_extractor.py

import re
from skills_db import TECHNICAL_SKILLS, SOFT_SKILLS

def extract_skills(text):
    text = text.lower()

    technical_found = []
    soft_found = []

    for skill in TECHNICAL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            technical_found.append(skill.title())

    for skill in SOFT_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            soft_found.append(skill.title())

    return {
        "technical_skills": list(set(technical_found)),
        "soft_skills": list(set(soft_found))
    }
