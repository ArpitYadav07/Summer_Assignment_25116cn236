# Write a program to Merge arrays.
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

merged = []

for i in arr1:
    merged.append(i)

for i in arr2:
    merged.append(i)

print("Merged array:", merged)