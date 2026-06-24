# Sort Words by Length
words = input("Enter words: ").split()

words.sort(key=len)

print(words)