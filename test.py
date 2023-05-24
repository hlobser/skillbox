from copy import deepcopy
n = int(input())
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix2 = deepcopy(matrix1)
for _ in range(1, m):
    result_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
    matrix2 = deepcopy(result_matrix)

for row in result_matrix:
    print(*row)