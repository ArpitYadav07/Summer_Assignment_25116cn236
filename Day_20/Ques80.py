# Write a program to Find column-wise sum. 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print(f"Sum of column {j+1} = {total}")