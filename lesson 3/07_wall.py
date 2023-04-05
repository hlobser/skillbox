# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x1, y1 = 0, -50
x2, y2 = 100, 0
i = 0 # смещение
for _ in range (20):
    i += 50
    y1 += 50
    y2 += 50
    x1 = -1000 + i
    x2 = -900 + i
    for _ in range(20):
        start = sd.get_point(x1, y1)
        finish = sd.get_point(x2, y2)
        sd.rectangle(start, finish, color=sd.COLOR_RED, width=2)
        x1 += 100
        x2 += 100
sd.pause()
