row = input().split()
result = [[]]
for i in range(1, len(row) + 1):
    for j in range(len(row) - i + 1):
        result.append(row[j: i + j])

print(result)
