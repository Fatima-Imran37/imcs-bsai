sentence = input("Enter a sentence: ")

print("Characters:", len(sentence))
print("Words:", len(sentence.split()))
print("Vowels:", sum(1 for c in sentence.lower() if c in "aeiou"))
print("Spaces:", sentence.count(" "))
print("Digits:", sum(1 for c in sentence if c.isdigit()))