# Write a program to Find row-wise sum.
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")