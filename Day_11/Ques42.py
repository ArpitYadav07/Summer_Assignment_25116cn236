# Write a program to Write function to find maximum
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
print("Maximum =", maximum(n, m))