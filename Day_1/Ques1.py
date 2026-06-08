# Write a program to Calculate sum of first N natural numbers
n=int(input("Enter the number "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"The sum of {n} natural number is {sum}")