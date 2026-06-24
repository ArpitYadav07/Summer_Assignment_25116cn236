# Find Common Characters in Strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

for ch in set(s1):
    if ch in s2:
        print(ch, end=" ")