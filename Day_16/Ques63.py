# Write a program to Find pair with given sum. 
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter required sum: "))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            found = True

if not found:
    print("No pair found")