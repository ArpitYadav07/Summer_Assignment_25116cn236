# Write a program to Check whether a number is prime
n=int(input("Enter the number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime")
            break
    else:
        print("Prime")
else:
    print("Not a prime")