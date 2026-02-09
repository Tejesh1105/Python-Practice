'''Write a Python program that:

Takes a sentence as input

Prints the number of words, unique words, and frequency of each word
'''




from collections import Counter

text = input("Enter text: ").lower()

words = text.split()

print("Number of words:", len(words))

unique_words = set(words)
print("Number of unique words:", len(unique_words))

freq = Counter(words)

print("Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")
