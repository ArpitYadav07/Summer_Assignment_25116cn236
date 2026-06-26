# Menu Driven String Operations System
s = input("Enter string: ")

print("1.Uppercase")
print("2.Reverse")

choice = int(input("Enter choice: "))

if choice == 1:
    print(s.upper())

elif choice == 2:
    print(s[::-1])