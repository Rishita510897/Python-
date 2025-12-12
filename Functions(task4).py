def welcome():
    print("Welcome to Python!")
welcome()
# 2
def greet(name):
    print("Hello!",name)
greet("Rishitha")
# 3
def square(n):
    return n*n
print(square(10))
#4
def calculator(a,b):
    return a+b,a-b,a*b
print(calculator(5,10))
#5
def country(name):
    print("I am from",name)
country("India")
# 6
def total(*nums):
    return sum(nums)
print(total(1,2,3,4))
# 7
def student_info(**data):
    for key,value in data.items():
        print(key,":",value)
student_info(name="Rishitha",age=20,course="Python")
# 8
def count_variables(text):
    vowels="aeiouAEIOU"
    c=0
    for ch in text:
        if ch in vowels:
            c+=1
    return c
print(count_variables("string"))
# 9
Cube = lambda n:n*n*n
print(Cube(6))

# 10
def unique_letters(text):
    result = []
    for ch in text:
        if ch not in result:
            result.append(ch)
    return "".join(result)
print(unique_letters("hello"))
