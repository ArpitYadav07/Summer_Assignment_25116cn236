# Write a program to Check strong number
n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total += fact
    temp = temp // 10

if total == n:
    print("Strong Number")
else:
    print("Not a Strong Number")