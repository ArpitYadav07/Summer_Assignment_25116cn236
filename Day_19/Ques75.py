# Write a program to Transpose matrix
A = [[1, 2],
     [3, 4]]

T = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        T[j][i] = A[i][j]

print("Transpose Matrix:")
for row in T:
    print(row)