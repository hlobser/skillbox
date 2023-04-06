# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def point(x, y):
    simple_draw.get_point(x, y)
    return simple_draw.get_point(x, y)


def smile_random(x, y, color):
    x1 = simple_draw.random_number(0, 400)
    y1 = simple_draw.random_number(0, 400)
    ellipse_start = point(x1, y1)
    ellipse_finish = point(x1 + x, y1 + y)
    simple_draw.ellipse(ellipse_start, ellipse_finish, color, width=1)
    left_eye_center = point(x1 + (x / 2) + x / 4, y1 + y / 2 + y / 8)
    right_eye_center = point(x1 + (x / 2) - x / 4, y1 + y / 2 + y / 8)
    simple_draw.circle(left_eye_center, radius=5, color=color, width=1)
    simple_draw.circle(right_eye_center, radius=5, color=color, width=1)
    mouth_coordinates_list = [point(x1 + (x / 2) + x / 4, y1 + y / 4), point(x1 + (x / 2) + x / 5, y1 + y / 5),
                              point(x1 + (x / 2) - x / 5, y1 + y / 5), point(x1 + (x / 2) - x / 4, y1 + y / 4)]
    simple_draw.lines(point_list=mouth_coordinates_list, color=color)


for _ in range(10):
    print(smile_random(100, 300, color=simple_draw.COLOR_RED))

simple_draw.pause()
