# Write a program to Remove duplicates from array.
arr = list(map(int, input("Enter elements: ").split()))

result = []

for i in arr:
    if i not in result:
        result.append(i)

print("Array after removing duplicates:", result)