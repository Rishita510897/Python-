# milestone2/skill_extractor.py

import spacy
from spacy.matcher import PhraseMatcher
from .skills_db import ALL_SKILLS


nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in ALL_SKILLS]
matcher.add("SKILLS", patterns)

def extract_skills(text: str):
    """
    Extract skills from resume or job description text.
    Returns a list of matched skill strings.
    """
    if not text:
        return []

    doc = nlp(text)
    matches = matcher(doc)

    found_skills = set()
    for match_id, start, end in matches:
        found_skills.add(doc[start:end].text)

    return list(found_skills)
