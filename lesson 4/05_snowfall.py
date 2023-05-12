# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
N = 20
snowflake_coordinate_list_x = []
snowflake_coordinate_list_y = []
snowflake_length_list = []

for _ in range(0, N):
    snowflake_coordinate_list_x.append(random.randrange(100, 500, 100))
    snowflake_coordinate_list_y.append(random.randrange(400, 550, 10))
    snowflake_length_list.append(random.randrange(10, 100, 10))


while True:
    sd.clear_screen()
    for i, _ in enumerate(snowflake_coordinate_list_x):
        point = sd.get_point(snowflake_coordinate_list_x[i], snowflake_coordinate_list_y[i])
        sd.snowflake(center=point, length=snowflake_length_list[i])
        snowflake_coordinate_list_y[i] -= 10
        if snowflake_coordinate_list_y[i] < snowflake_length_list[i]:
            snowflake_coordinate_list_y[i] += 10
    else:
        sd.sleep(0.1)
        if snowflake_coordinate_list_y == snowflake_length_list:
            break
        continue
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
