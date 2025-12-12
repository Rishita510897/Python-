#1
import csv
with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","grade"])
    writer.writerow(["Rishi",20,"A"])
    writer.writerow(["Siri",19,"A"])
    writer.writerow(["Ruthi",18,"B"])

#2
import csv
with open("employees.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#3
import csv
with open("products.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[0])

#4
import csv
with open("data.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        for key,value in row.items():
            print(key,":",value)
        print()

#5
import csv
with open("marks.csv","a",newline="") as file:
    
