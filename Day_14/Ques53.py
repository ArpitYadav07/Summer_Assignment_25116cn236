# Write a program to Linear search
# Linear Search
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter element to search: "))

for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")