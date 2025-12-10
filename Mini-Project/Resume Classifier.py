skills=input("Enter your skills: \n").lower()
skills_list=[skill.strip() for skill in skills.split(",")]
data_ml_keywords = ["python", "machine learning", "ml", "data science", "sql", "pandas", "numpy", "ai"]
web_keywords = ["html", "css", "javascript", "react", "node", "php", "frontend", "backend"]
software_keywords = ["java", "c++", "c", "c#", "software development", "oop", "testing"]
category="None"
for skill in skills_list:
    if skill in data_ml_keywords:
        category="Data / Machine Learning"
        break
    elif skill in web_keywords:
        category="Web Development"
        break
    elif skill in software_keywords:
        category="Software development"
        break
print("Predicted Category:",category)

#Output
"""
Enter your skills: 
python,sql,pandas
Predicted Category: Data / Machine Learning
"""