# Write a program to Union of arrays.
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

union = []

for i in arr1:
    if i not in union:
        union.append(i)

for i in arr2:
    if i not in union:
        union.append(i)

print("Union of arrays:", union)