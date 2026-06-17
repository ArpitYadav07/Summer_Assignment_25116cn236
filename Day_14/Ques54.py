# Write a program to Frequency of an element.
# Frequency of an element in an array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter element to find frequency: "))
count = 0

for i in arr:
    if i == key:
        count += 1

print("Frequency =", count)