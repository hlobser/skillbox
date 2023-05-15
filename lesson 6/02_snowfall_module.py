# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowfall, draw_snowfalls_colored, move_snowfall, numbers_floor, del_snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#     #  нарисовать_снежинки_цветом(color=sd.background_color)
#     #  сдвинуть_снежинки()
#     #  нарисовать_снежинки_цветом(color)
#     #  если есть номера_достигших_низа_экрана() то
#     #       удалить_снежинки(номера)
#     #       создать_снежинки(count)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()



create_snowfall(5)
while True:
    draw_snowfalls_colored(color=sd.background_color)
    move_snowfall()
    draw_snowfalls_colored(color=sd.COLOR_CYAN)
    if numbers_floor() != []:
        del_snowfall()
        create_snowfall(len(numbers_floor()))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

