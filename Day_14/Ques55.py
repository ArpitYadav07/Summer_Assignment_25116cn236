# Write a program to Second largest element
# Find second largest element in an array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
second = arr[0]

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest element =", second)