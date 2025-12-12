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
    writer=csv.writer(file)
    writer.writerow(["Rishita","Python",95])

#6
import csv
cnt=0
with open("data.csv") as file:
    reader=csv.reader(file)
    next(reader)
    for _ in reader:
        cnt+=1
print("Total rows:",cnt)

#7
import csv
t=0
with open("sales.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        t+=float(row["price"])*int(row["quantity"])
print("Total Sales:",t)

#8
import csv
data=[
    [1,"Riya"].
    [2,"Aman"],
    [3,"Kiran"]
]
with open("output.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["id","name"])
    writer.writerows(data)

#9
import csv
with open("people.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        if int(row["age"])>30:
            print(row)

#10
import csv
with open("source.csv") as src,open("copy.csv","w",neline="") as dest:
    reader=csv.reader(src)
    writer=csv.writer(dest)
    for row in reader:
        writer.writerow(row)
        

