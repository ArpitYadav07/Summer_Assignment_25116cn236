# Menu Driven Array Operations System
arr = list(map(int, input("Enter array: ").split()))

print("1.Sort")
print("2.Reverse")

choice = int(input("Enter choice: "))

if choice == 1:
    arr.sort()
    print(arr)

elif choice == 2:
    print(arr[::-1])