# Write a program to Find maximum frequency element. 
arr = list(map(int, input("Enter elements: ").split()))

max_freq = 0
max_element = arr[0]

for i in arr:
    freq = 0
    for j in arr:
        if i == j:
            freq += 1

    if freq > max_freq:
        max_freq = freq
        max_element = i

print("Maximum frequency element:", max_element)
print("Frequency:", max_freq)