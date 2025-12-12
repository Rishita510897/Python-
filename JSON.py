#1
import json
json_str="{'name':'Alex','age':22,'city':'Chennai'}".replace("'",'"')
data=json.loads(json_str)
print(data)
#Output
#{'name': 'Alex', 'age': 22, 'city': 'Chennai'}
#2
data = {'id': 101, 'product': 'Laptop', 'price': 55000}
json_str = json.dumps(data)
print(json_str)
# Output
# {"id": 101, "product": "Laptop", "price": 55000}
#3
with open("data.json") as file:
    data = json.load(file)
for key, value in data.items():
    print(key, ":",value)
#Output
"""
name : Alex
age : 22
city : Chennai
"""
#4
data = {'name': 'Mia', 'age': 24, 'grade': 'A'}
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

#5
data = {'employee': {'name': 'John', 'age': 30, 'department': 'HR'}}
print(data['employee']['department'])
# Output
# HR
#6
data = {'name': 'Raj', 'age': 45}
data['age'] = 50  
json_str = json.dumps(data)
print(json_str)
#Output
#{"name": "Raj", "age": 50}
#7
colors = json.loads('["red", "green", "blue"]')
print(colors[1])
#Output
#green
#8

data = {'users': [{'id': 1, 'name': 'Alex'}, {'id': 2, 'name': 'Mia'}]}
for user in data['users']:
    print(user['name'])
# Output
"""
Alex
Mia
"""
#9
data = {'name': 'Sam', 'age': 28}
data['country'] = 'India'
json_str = json.dumps(data)
print(json_str)
# Output
# {"name": "Sam", "age": 28, "country": "India"}
#10

items = [
    {'item': 'Pen', 'price': 10},
    {'item': 'Book', 'price': 50},
    {'item': 'Bag', 'price': 700}
]
with open("items.json", "w") as file:
    json.dump(items, file, indent=4)
total = sum(item['price'] for item in items)
print("Total Cost:", total)
# Output
#Total Cost: 760