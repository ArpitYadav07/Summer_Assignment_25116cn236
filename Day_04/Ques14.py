# Write a program to Find nth Fibonacci term
n = int(input("Enter the term number: "))
a = 0
b = 1
for i in range(n - 1):
    c = a + b
    a = b
    b = c
print("The", n, "th Fibonacci term is", a)