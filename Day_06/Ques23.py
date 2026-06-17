# Write a program to Count set bits in a number
n = int(input("Enter a number: "))
count = 0
while n > 0:
    if n % 2 == 1:
        count += 1
    n = n // 2
print("Number of set bits =", count)