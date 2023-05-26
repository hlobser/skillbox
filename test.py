m, n = int(input()), int(input())
first_set = set([input() for _ in range(n)])
empty_set = set()
if m == 1:
    print(*sorted(first_set), sep='\n')
else:
    for i in range(m-1):
        for j in range(int(input())):
            empty_set.add(input())
        first_set.intersection_update(empty_set)
        empty_set.clear()
    first_set = sorted(first_set)
    for row in first_set:
        print(row)
fuck off