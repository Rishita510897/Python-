# 1 to 10
for i in range(1,11):
    print(i)   
# 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)
# each character
for ch in 'Python':
    print(ch)
# 5 to 1
i=5
while i>=1:
    print(i)
    i-=1
# sum from 1 to 50
total=0
for i in range(1,51):
    total+=i
print("sum:",total)
# multiplication table of 5
for i in range(1,11):
    print(5,"X",i,"=",5*i)
# count vowels
text="Programming"
vowels="aeiouAEIOU"
c=0
for ch1 in text:
    if ch1 in vowels:
        c+=1
print("Vowel count:",c)
# reverse string
s="PythonLoops"
rev=""
for ch in s:
    rev=ch+rev
print("reversed:",rev)
# 1-10 skip 5
for i in range(1,11):
    if i==5:
        continue
    print(i)
# 1-20 stop at 13
for i in range(1,21):
    if i==13:
        break
    print(i)
# prime or not
n=int(input())
c1=0
for i in range(2,n):
    if n%i==0:
        c1+=1
if c1>2:
    print("not a prime")
else:
    print("prime")
# count 
text="mississippi"
f={}
for ch in text:
    if ch in f:
        f[ch]+=1
    else:
        f[ch]=1
print(f)
# pattern
for i in range(1,6):
    print("*"*i)
# find largest
num="5847361"
lar=0
for ch in num:
    if int(ch)>lar:
        lar=int(ch)
print("largest:",lar)

# pattern
for i in range(5,0,-1):
    print("*"*i)

