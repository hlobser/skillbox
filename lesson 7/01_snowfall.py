# -*- coding: utf-8 -*-
from random import randrange

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x, self.y = randrange(100, 500, 40), randrange(400, 550, 10)
        self.length = randrange(10, 50, 10)


    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)


    def move(self, delta_y):
        self.y -= delta_y

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length)


    def can_fall(self):
        return self.y > self.length




def get_flakes(count):
    flakes_list = []
    for _ in range(count):
        flake = Snowflake()
        flakes_list.append(flake)
    return flakes_list

def get_fallen_flakes():
    count = 0
    if flake.can_fall():
        count += 1
    return count

def append_flakes(count):
    for _ in range(count):
        flake = Snowflake()
        flakes.append(flake)


    # TODO здесь ваш код


# flake = Snowflake()
# while True:
#     flake.clear_previous_picture()
#     flake.move(10)
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=2)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move(10)
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
