# Menu Driven Calculator
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print(a + b)

    elif choice == 2:
        print(a - b)

    elif choice == 3:
        print(a * b)

    elif choice == 4:
        print(a / b)