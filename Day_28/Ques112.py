# Contact Management System
contacts = {}

while True:
    name = input("Name: ")
    number = input("Number: ")

    contacts[name] = number

    ch = input("Add more? (y/n): ")

    if ch == "n":
        break

print(contacts)