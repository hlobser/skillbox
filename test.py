n, k = int(input()), int(input())
list = [i for i in range(1, n+1)]
del_index = k - 1
del list[del_index]
while len(list) > 1:
    del_index = (del_index + k - 1) % len(list)
    del list[del_index]
print(*list)