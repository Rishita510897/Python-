import re
job_title=input("Enter job title: \n")
clean_title=re.sub(r'[^A-Za-z0-9 ]', '',job_title)
normalized_title=clean_title.title()
print("Normalized Job Title:",normalized_title)


#Output
"""
Enter job title: 
senior@# data--scientist!!
Normalized Job Title: Senior Datascientist
"""