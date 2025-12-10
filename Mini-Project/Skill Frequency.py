resume_text=input("Enter resume text: \n").lower()
skill=input("Enter skill: \n").lower()
cnt=resume_text.count(skill)
print(f"Skill appears {cnt} times.")

#Output
"""
Enter resume text: 
I have experience in Python,machine learning, and Python automation.
Enter skill: 
python
Skill appears 2 times.
"""