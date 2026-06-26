# Student Record Management System
students = {}

while True:
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    students[name] = marks

    ch = input("Add more? (y/n): ")

    if ch == "n":
        break

print(students)