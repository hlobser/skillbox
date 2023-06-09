from random import sample, choice

n = int(input())
names, secret_santa_dict, x = {input() for _ in range(n)}, {}, 0
for name in names.copy():
    if names == {name}:
        secret_santa_dict[x], secret_santa_dict[name] = name, x
    else:
        rand_name = choice(list(names - {name}))
        secret_santa_dict[name] = rand_name
        names -= {rand_name}
        x = name
for key, value in secret_santa_dict.items():
    print(f'{key} - {value}')














#
# n = int(input())
# names = []
# for _ in range(n):
#     names.append(input())
# secret_santa = sample(names, k=len(names))
# flag = True
# while flag:
#     flag = False
#     for i in range(len(names)):
#         if names[i] == secret_santa[i]:
#             secret_santa = sample(names, k=len(names))
#             flag = True
# for i in range(len(names)):
#     print(f'{names[i]} - {secret_santa[i]}')