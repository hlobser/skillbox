list_input = input().split()
for k in range(len(list_input)):
    list_input[k] = int(list_input[k])
count = 0
for i in range(len(list_input) - 1):
    for j in range(len(list_input) - i - 1):
        if list_input[j + 1] > list_input[j]:
          count += 1
    break
print(count)
