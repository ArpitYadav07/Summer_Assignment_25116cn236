# Write a program to Write function to find factorial. 
# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))