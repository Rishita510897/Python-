import json
import numpy as np

def to_python_type(value):
    """Convert numpy data types to native Python types"""
    if isinstance(value, (np.float32, np.float64)):
        return float(value)
    if isinstance(value, dict):
        return {k: to_python_type(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_python_type(v) for v in value]
    return value

def generate_skill_gap_report(resume_skills, jd_skills, best_matches, alignment_score):
    report = {
        "overall_alignment": round(float(alignment_score) * 100, 2),
        "resume_skills": resume_skills,
        "job_description_skills": jd_skills,
        "matched_skills": [],
        "partial_skills": [],
        "missing_skills": []
    }

    for jd_skill, data in best_matches.items():
        entry = {
            "job_skill": jd_skill,
            "best_resume_match": data["best_resume_skill"],
            "similarity_score": round(float(data["score"]), 3),
            "top_3_matches": {
                k: round(float(v), 3)
                for k, v in data["top_3"].items()
            }
        }

        if data["score"] >= 0.8:
            report["matched_skills"].append(entry)
        elif data["score"] >= 0.5:
            report["partial_skills"].append(entry)
        else:
            report["missing_skills"].append(entry)

    return to_python_type(report)

def save_report(report, filename="skill_gap_report.json"):
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
