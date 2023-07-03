import re
with open(r'C:\Users\Sergey\projects\skillbox\nums.txt', encoding='utf-8', mode='r') as file:
    sp = [re.findall('\d+', i) for i in file.readlines()]
    print(sum([int(i)  for lst in sp for i in lst]))
lalalalalala