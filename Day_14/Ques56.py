# Write a program to Find duplicates in array
# Find duplicates in an array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Duplicate elements are:")

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])
            break