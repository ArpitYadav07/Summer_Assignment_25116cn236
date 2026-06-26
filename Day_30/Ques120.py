# Complete Mini Project Using Arrays, Strings and Functions
students = {}

def add_student():
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[name] = marks

def display():
    for name, marks in students.items():
        print(name, marks)

while True:
    print("1.Add Student")
    print("2.Display")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display()

    elif choice == 3:
        break