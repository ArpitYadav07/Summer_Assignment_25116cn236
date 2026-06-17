# Write a program to Print Armstrong numbers in a range
n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
for num in range(n, m + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10
        
    if total == num:
        print(num)