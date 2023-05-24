n1, m1 = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n1)]
spase = input()
n2, m2 = [int(i) for i in input().split()]
matrix_2 = [[int(i) for i in input().split()] for _ in range(n2)]

matrix_product = [[0] * m2 for _ in range(n1)]
for i_product in range(n1):
    for j_product in range(m2):
        for j in range(m1):
            matrix_product[i_product][j_product] += matrix_1[i_product][j]*matrix_2[j][j_product]


for k in matrix_product:
    print(*k)