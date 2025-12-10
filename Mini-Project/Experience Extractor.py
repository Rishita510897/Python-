def main():
    print("EXPERIENCE EXTRACTOR")
    sentence=input("Enter sentence:\n")
    words=sentence.split()
    years=0
    for i in words:
        if i.isdigit():
            years=i
            break
    if years:
        print("Experienced Detected: ",years)
    else:
        print("\nNo experience years detected.")
if __name__=="__main__":
    main()


# Output
"""
EXPERIENCE EXTRACTOR
Enter sentence:
I have 3 years of experience in Python.
Experienced Detected:  3
"""