# Write a program to Sort array in descending order. 
arr = list(map(int, input("Enter elements: ").split()))

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Array in descending order:", arr)