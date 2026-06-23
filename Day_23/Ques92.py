# Find Maximum Occurring Character
s = input("Enter a string: ")

max_char = s[0]
max_count = s.count(s[0])

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Character =", max_char)