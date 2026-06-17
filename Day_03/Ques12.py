# Write a program to Find LCM of two numbers
n=int(input("Enter the number: "))
m=int(input("Enter the number: "))
greater = max(n, m)
while True:
    if greater % n == 0 and greater % m == 0:
        print("LCM =", greater)
        break
    greater += 1