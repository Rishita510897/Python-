def clean_skill_list(skills):
    cleaned = set()
    for skill in skills:
        s = skill.lower().strip()
        if len(s) > 1:
            cleaned.add(s)
    return sorted(list(cleaned))
