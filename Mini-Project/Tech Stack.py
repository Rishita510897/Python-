tech_list = input("Enter tools:\n").lower().split(",")
tech_list = [t.strip() for t in tech_list]
programming_lang = ["python", "java", "c", "c++", "c#", "javascript", "go", "ruby", "kotlin"]
databases = ["mysql", "postgresql", "mongodb", "oracle", "sql server", "sqlite", "redis"]
frameworks = ["django", "flask", "react", "angular", "spring", "node", "fastapi", "laravel"]
lang_count = 0
db_count = 0
fw_count = 0
for tech in tech_list:
    if tech in programming_lang:
        lang_count += 1
    elif tech in databases:
        db_count += 1
    elif tech in frameworks:
        fw_count += 1
print("\nSummary")
print("Programming Languages:", lang_count)
print("Databases:", db_count)
print("Frameworks:", fw_count)

#Output
"""
Enter tools:
Python,MySQL,Django,Java,React,MongoDB

Summary
Programming Languages: 2
Databases: 2
Frameworks: 2
"""