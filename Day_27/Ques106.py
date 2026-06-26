# Employee Management System
employees = {}

while True:
    emp = input("Employee Name: ")
    salary = input("Salary: ")

    employees[emp] = salary

    ch = input("Add more? (y/n): ")

    if ch == "n":
        break

print(employees)