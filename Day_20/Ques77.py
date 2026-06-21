# Write a program to Multiply matrices. 
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible")
else:
    matrix1 = []
    matrix2 = []

    print("Enter first matrix:")
    for i in range(r1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    print("Enter second matrix:")
    for i in range(r2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(*row)