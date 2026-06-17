# Write a program to Find sum and average of array
# Find sum and average of array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = 0
for i in arr:
    total += i
average = total / n

print("Sum =", total)
print("Average =", average)