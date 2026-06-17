# Write a program to Move zeroes to end
arr = list(map(int, input("Enter elements: ").split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr.append(0)
        arr.pop(i)

print("Array after moving zeroes:", arr)