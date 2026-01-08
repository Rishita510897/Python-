import spacy
from spacy.matcher import PhraseMatcher
from skills_db import TECHNICAL_SKILLS, SOFT_SKILLS

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text.lower())
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

    matcher.add("TECH", [nlp.make_doc(s) for s in TECHNICAL_SKILLS])
    matcher.add("SOFT", [nlp.make_doc(s) for s in SOFT_SKILLS])

    tech, soft = set(), set()

    for match_id, start, end in matcher(doc):
        skill = doc[start:end].text
        label = nlp.vocab.strings[match_id]
        if label == "TECH":
            tech.add(skill)
        else:
            soft.add(skill)

    return list(tech), list(soft)


def assign_confidence(skills):
    base = 85
    return {skill: min(95, base + i) for i, skill in enumerate(skills)}
