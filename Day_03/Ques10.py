# Write a program to Print prime numbers in a range
n=int(input("Enter range starting point: "))
m=int(input("Enter range ending point: "))
for num in range(n,m+1):
    if num>1:
        for divisor in range(2,int(num**0.5) +1):
            if num%divisor==0:
                break 
        else:
            print(f"{num} is Prime")   
    