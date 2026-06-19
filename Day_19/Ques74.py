# Write a program to Subtract matrices
# Matrix Subtraction

A = [[5, 6],
     [7, 8]]

B = [[1, 2],
     [3, 4]]

C = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] - B[i][j]

print("Result:")
for row in C:
    print(row)