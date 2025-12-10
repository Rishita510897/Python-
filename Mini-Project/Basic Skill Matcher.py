def main():
    print("Basic Skill Matcher")
    resume_input=input("Enter resume skills:\n")
    job_input=input("Enter job required skills:\n")
    resume_skills=normalize(resume_input)
    job_skills=normalize(job_input)
    matched=resume_skills & job_skills
    missing=job_skills-resume_skills
    if matched:
        print("matched skills")
    else:
        print("Not matched skills")
    if missing:
        print("missing skills")
    else:
        print("not missing any skills")
if __name__=="__main__":
    main()
    


