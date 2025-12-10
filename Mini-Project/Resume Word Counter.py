def main():
    print("RESUME WORD COUNTER")
    text=input("Enter your resume text")
    words=text.lower().split()
    total_words=len(words)
    unique_words=len(set(words))
    if words:
        most_common_word=max(set(words),key=words.count)
        count=words.count(most_common_word)
    else:
        most_common_word="None"
        count=0
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Most repeated word:", most_common_word, "appeared", count, "times")

if __name__=="__main__":
    main()