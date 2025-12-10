text=input("Enter text:\n")
words=text.split()
email=None
for word in words:
    if "@" in word:
        email=word
        break
if email:
    print("Extracted Email:",email)
else:
    print("No email detected.")

#Output
"""
Enter text:
contact me at rishitha@gmail.com for more details.
Extracted Email: rishitha@gmail.com
"""

