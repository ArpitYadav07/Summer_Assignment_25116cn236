# Write a program to Count even and odd elements. 
# Count even and odd elements in an array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even elements =", even)
print("Odd elements =", odd)