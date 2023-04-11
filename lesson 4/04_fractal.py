# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle+30, length=length)
#     v2 = sd.get_vector(start_point=point, angle=angle-30, length=length)
#     v1.draw()
#     v2.draw()
#     return v1.end_point, v2.end_point


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

def draw_branches(point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(start_point=point, angle=angle+30, length=length)
    v2 = sd.get_vector(start_point=point, angle=angle-30, length=length)
    v1.draw()
    v2.draw()
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_angle_minus = angle - 30 - angle * random.uniform(0.0, 0.4)
    next_angle_plus = angle + 30 + angle * random.uniform(0.0, 0.4)
    next_length = length * .75 + .75 * random.uniform(0.0, 0.2)
    draw_branches(point=next_point_1, angle=next_angle_plus, length=next_length)
    draw_branches(point=next_point_2, angle=next_angle_minus, length=next_length)


# 3) первоначальный вызов:
root_point = sd.get_point(300, 30)
draw_branches(point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
# next_angle_plus = angle + angle * random.uniform(0.0, 0.4)
#
# next_angle_minus = angle - angle * random.uniform(0.0, 0.4)
sd.pause()


