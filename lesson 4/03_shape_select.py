# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

color = sd.COLOR_PURPLE
def point(x, y):
    sd.get_point(x, y)
    return sd.get_point(x, y)


def polygon(number_of_angles, start_point, angle, length, color):
    for i in range(1, number_of_angles+1):
        vector = sd.vector(start=start_point, angle=angle + (360 / number_of_angles * i),
                           length=length, color=color)
        start_point = vector
    return vector


print('Возможные фигуры:\n'
      '0: треугольник\n'
      '1: квадрвт\n'
      '2: пятиугольник\n'
      '3: шестиугольник')
print('введите желаемую фигуру:')
num_of_polygon = int(input())
for j in range(0, 4):
    if j == num_of_polygon:
        polygon(number_of_angles=j+3, start_point=point(350, 250), angle=0, length=100, color=color)
        break
else:
    print('вы ввели некорректный номер')

sd.pause()
