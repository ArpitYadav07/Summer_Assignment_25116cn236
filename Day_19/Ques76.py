# Write a program to Find diagonal sum
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum = 0

for i in range(len(A)):
    diagonal_sum += A[i][i]

print("Diagonal Sum:", diagonal_sum)