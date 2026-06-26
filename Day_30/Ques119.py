# Mini Employee Management System
employees = {}

while True:
    name = input("Name: ")
    salary = input("Salary: ")

    employees[name] = salary

    if input("Continue? (y/n): ") == "n":
        break

print(employees)