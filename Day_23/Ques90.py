# Find First Repeating Character
s = input("Enter a string: ")

seen = []

for ch in s:
    if ch in seen:
        print("First Repeating Character =", ch)
        break
    seen.append(ch)