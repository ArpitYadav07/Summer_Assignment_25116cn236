# Write a program to Write function for palindrome
# Function to check palindrome
def palindrome(n):
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return original == rev

num = int(input("Enter a number: "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")