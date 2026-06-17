# Write a program to Find x^n without pow()
x = int(input("Enter the base: "))
n = int(input("Enter the power: "))
result = 1
for i in range(n):
    result *= x
print("Answer =", result)