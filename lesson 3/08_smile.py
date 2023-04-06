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
def smile_random():
    x1 = simple_draw.random_number(0, 400)
    y1 = simple_draw.random_number(0, 400)
    purple = simple_draw.COLOR_PURPLE
    ellipse_start = point(x1, y1)
    ellipse_finish = point(x1+150, y1+100)
    simple_draw.ellipse(ellipse_start, ellipse_finish, purple, width=1)
    left_eye_center = point(x1+45, y1+60)
    right_eye_center = point(x1+105, y1+60)
    simple_draw.circle(left_eye_center, radius=5, color=purple, width=1)
    simple_draw.circle(right_eye_center, radius=5, color=purple, width=1)
    mouth_coordinates_list = [point(x1 + 40, y1 + 30), point(x1 + 50, y1 + 20), point(x1 + 100, y1 + 20), point(x1 + 110, y1 + 30)]
    simple_draw.lines(point_list=mouth_coordinates_list, color=purple)


for _ in range(10):
    print(smile_random())


simple_draw.pause()
