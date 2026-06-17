# Write a program to Find GCD of two numbers
n= int(input("Enter first number: "))
m= int(input("Enter second number: "))
gcd = 1
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        gcd = i

print("GCD =", gcd)