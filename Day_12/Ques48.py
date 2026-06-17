# Write a program to Write function for perfect number.
# Function to check perfect number
def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

num = int(input("Enter a number: "))
if perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")