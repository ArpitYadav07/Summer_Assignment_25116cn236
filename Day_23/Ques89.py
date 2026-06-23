# Find First Non-Repeating Character
s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First Non-Repeating Character =", ch)
        break