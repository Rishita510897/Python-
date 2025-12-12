"""
# Extract first 3 characters
text = 'Python'
print(text[:3])
# convert to lowercase
name='hello WORLD'
print(name.lower())
# remove extra spaces
msg='Welcome to Python'
print(msg.strip())
# find length
word='Programming'
print(len(word))
# split based on comma
text='apple,banana,grape'
print(text.split(','))
# replace java with python
text1='I love Java'
print(text1.replace('Java','Python'))
# extract science
line='Data Science'
print(line.split()[1])
# get the last character
text2='Python'
print(text[-1])
# check if python is present
sentence='Learning Python is fun'
res='Python' in sentence
print(res)
# join list into a sentence 
words=['Python','is','easy']
result=' '.join(words)
print(result)
"""

# Extract using slicing
text='Programming'
print(text[6:])
# count how many times hello appears
s='Hello,Python,Hello,World'
print(s.count('Hello'))
# reverse string
word='Development' 
print(word[::-1])
# replace awesome with powerfulonly if python exists
sentence='Python is awesome'
if 'Python' in sentence:
    res=sentence.replace('awesome','powerful')
    print(res)
# count occurrences 
t='aaabbbcccaaa'
sub='aaa'
count=0
for i in range(len(t)-len(sub)+1):
    if t[i:i+len(sub)]==sub:
        count+=1
print("Occurrences of 'aaa':",count)

# extract username and domain
email='username@example.com'
username,domain=email.split('@')
print("Username:",username)
print("Domain:",domain)
# extract numeric value
line='The price is 1500 rupees'
number=''
for word in line.split():
    if word.isdigit():
        number=word
print("Number extracted:",number)
# split
words='python-is-simple-and-powerful'
r=' '.join(words.split('-'))
print("Rejoined sentence:",r)
# remove numbers
t2='Hello123World45Python'
r1=""
for ch in t2:
    if ch.isalpha():
        r1+=ch
print(r1)
# find first character
t1='Mississippi'
seen=set()
first_repeat=None
for ch in t1:
    if ch in seen:
        first_repeat=ch
        break
    seen.add(ch)
print("First repeated character:",first_repeat)