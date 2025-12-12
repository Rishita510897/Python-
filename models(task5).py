# 1
import math
print(math.sqrt(9))
# 2
print(math.floor(5.67))
print(math.ceil(5.67))
# 3
import random 
print(random.randint(1,100))
# 4
for _ in range(5):
    print(random.randint(10,20))
# 5
import datetime
print(datetime.date.today())
# 6
today=datetime.date.today()
print(today.year,today.month,today.day)
# 7
import os
print(os.getcwd())
# 8
print(os.listdir())
# 9
import sys
print(sys.version)
# 10
import json
data = '{"name":"Rishitha","age":"20"}'
print(json.loads(data))
# 11
print(math.cos(0))
print(math.sin(math.radians(90)))
print(math.log(10))
# 12
rolls=[random.randint(1,6) for _ in range(10)]
print(rolls)
# 13
today=datetime.date.today()
birthday=datetime.date(today.year,9,14)
if birthday < today:
    birthday = datetime.date(today.year + 1, 9, 14)
print((birthday - today).days, "days left")
# 14
d = datetime.datetime.strptime("2022-05-15", "%Y-%m-%d")
new_date = d + datetime.timedelta(days=30)
print(new_date)
# 15
#os.mkdir("backup")
# 16
import json
data = {"name": "Rishita", "score": 95}
print(json.dumps(data))
# 17
import re
text = "Hello123Python456"
print(re.findall(r"\d+", text))
# 18
import re
text = "Hello World"
print(bool(re.match(r"Hello", text)))
# 19
import statistics
nums = [1, 2, 2, 3, 4]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))
# 20
import time
start = time.time()
for i in range(1, 1_000_001):
    pass
end = time.time()
print("Time taken:", end - start, "seconds")

