# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
x1, y1 = 50, 50
x2, y2 = 350, 450
for i in rainbow_colors:
    start_point = sd.get_point(x1, y1)
    end_point = sd.get_point(x2, y2)
    sd.line(start_point, end_point, color=i, width=4)
    x1 += 5
    x2 += 5
sd.clear_screen()
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
center = sd.get_point(500, -500)
radius = 700
for i in rainbow_colors:
    sd.circle(center, radius, i, width=15)
    radius += 15
sd.pause()
