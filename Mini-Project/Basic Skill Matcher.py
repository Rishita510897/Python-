def main():
    print("Basic Skill Matcher")
    resume_input=input("Enter resume skills:\n")
    job_input=input("Enter job required skills:\n")
    resume_skills=set(skill.strip().lower() for skill in resume_input.split(","))
    job_skills=set(skill.strip().lower() for skill in job_input.split(","))
    matched=resume_skills & job_skills
    missing=job_skills-resume_skills
    if matched:
        print("matched skills:"," ,".join(matched))
    else:
        print("Not matched skills")
    if missing:
        print("missing skills:"," ,".join(missing))
    else:
        print("not missing any skills")
if __name__=="__main__":
    main()
    


