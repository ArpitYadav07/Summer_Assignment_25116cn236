# Write a program to Write function for Armstrong
# Function to check Armstrong number
def armstrong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 3
        n = n // 10
    return total == original

num = int(input("Enter a number: "))
if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")