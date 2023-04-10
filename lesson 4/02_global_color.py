# -*- coding: utf-8 -*-
import simple_draw
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
red = sd.COLOR_RED
orange = sd.COLOR_ORANGE
yellow = sd.COLOR_YELLOW
green = sd.COLOR_GREEN
cyan = sd.COLOR_CYAN
blue = sd.COLOR_BLUE
purple = sd.COLOR_PURPLE
# colors_list =[red, orange, yellow, green, cyan, blue, purple]
colors_list = [
    {'red': red},
    {'orange': orange},
    {'yellow': yellow},
    {'green': green},
    {'cyan': cyan},
    {'blue': blue},
    {'purple': purple},
]
print('Возможные цвета: \n')
for num, colors_dict in enumerate(colors_list):
    print(num, list(colors_dict.keys())[0])


color_num = int(input())
for num, colors_dict in enumerate(colors_list):
    if num == color_num:
        color = list(colors_dict.values())[0]

def point(x, y):
    sd.get_point(x, y)
    return sd.get_point(x, y)


def polygon(number_of_angles, start_point, angle, length, color):
    for i in range(1, number_of_angles+1):
        vector = sd.vector(start=start_point, angle=angle + (360 / number_of_angles * i),
                           length=length, color=color)
        start_point = vector
    return vector


def triangle(point, angle, length, color):
    polygon(3, start_point=point, angle=angle, length=length, color=color)


def sqare(point, angle, length, color=1):
    polygon(4, start_point=point, angle=angle, length=length, color=color)


def pentagon(point, angle, length, color):
    polygon(5, start_point=point, angle=angle, length=length, color=color)


def hexagon(point, angle, length, color):
    polygon(6, start_point=point, angle=angle, length=length, color=color)


triangle(point=point(500, 300), angle=5, length=150, color=color)
sqare(point=point(200, 300), angle=12, length=100, color=color)
pentagon(point=point(500, 50), angle=20, length=100, color=color)
hexagon(point=point(200, 50), angle=0, length=100, color=color)
sd.pause()

