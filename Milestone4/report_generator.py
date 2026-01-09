import json
from datetime import datetime

def generate_skill_gap_report(resume_skills, jd_skills, matches, score):
    matched = []
    partial = []
    missing = []

    for r, data in matches.items():
        if data["score"] >= 0.75:
            matched.append(r)
        elif data["score"] >= 0.5:
            partial.append(data)
    
    for js in jd_skills:
        if js not in [v["job_skill"] for v in matches.values()]:
            missing.append(js)

    return {
        "overall_score": round(score * 100, 2),
        "matched_skills": matched,
        "partial_skills": partial,
        "missing_skills": missing
    }

def save_report(report):
    filename = f"skill_gap_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
