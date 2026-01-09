import spacy
from spacy.matcher import PhraseMatcher

# Load small English model
nlp = spacy.load("en_core_web_sm")

TECH_SKILLS = [
    "python", "java", "c++", "javascript", "html", "css",
    "react", "node.js", "django", "flask", "sql", "excel",
    "git", "docker", "aws", "linux", "tensorflow", "pandas",
    "numpy", "matplotlib", "scikit-learn", "machine learning"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving",
    "time management", "adaptability", "critical thinking",
    "creativity", "collaboration", "organization"
]

# PhraseMatchers
tech_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
soft_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

tech_patterns = [nlp(skill.lower()) for skill in TECH_SKILLS]
soft_patterns = [nlp(skill.lower()) for skill in SOFT_SKILLS]

tech_matcher.add("TECH_SKILLS", tech_patterns)
soft_matcher.add("SOFT_SKILLS", soft_patterns)


def extract_skills(text):
    """Extract technical and soft skills from text."""
    doc = nlp(text.lower())
    tech_matches = tech_matcher(doc)
    soft_matches = soft_matcher(doc)

    tech_skills = list({doc[start:end].text.strip() for _, start, end in tech_matches})
    soft_skills = list({doc[start:end].text.strip() for _, start, end in soft_matches})

    return tech_skills, soft_skills


def assign_confidence(skills):
    """Assign dummy confidence for demo purposes."""
    return {skill: min(100, 60 + i * 5) for i, skill in enumerate(skills)}
