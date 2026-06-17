# Write a program to Find common elements.
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

common = []

for i in arr1:
    if i in arr2 and i not in common:
        common.append(i)

print("Common elements:", common)