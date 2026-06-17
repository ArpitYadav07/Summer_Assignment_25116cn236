# Write a program to Input and display array
# Input and display array (list)

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array elements are:")
for i in arr:
    print(i, end=" ")
