from random import randrange
import simple_draw as sd



def create_snowfall(num):
    global snowflake_coordinate_list_x
    global snowflake_coordinate_list_y
    snowflake_coordinate_list_x = []
    snowflake_coordinate_list_y = []
    for _ in range(0, num):
        snowflake_coordinate_list_x.append(randrange(100, 500, 100))
        snowflake_coordinate_list_y.append(randrange(400, 550, 10))


def draw_snowfalls_colored(color):
    for i in range(len(snowflake_coordinate_list_x)):
        point = sd.get_point(snowflake_coordinate_list_x[i], snowflake_coordinate_list_y[i])
        sd.snowflake(center=point, length=50, color=color)


def move_snowfall():
    for i in range(len(snowflake_coordinate_list_y)):
        snowflake_coordinate_list_y[i] -= 10
    sd.sleep(0.1)

def numbers_floor():
    numbers_floor_list = []
    for i in range(len(snowflake_coordinate_list_y)):
        if snowflake_coordinate_list_y[i] == 50:
            numbers_floor_list.append(i)
    return numbers_floor_list


def del_snowfall():
    for i in numbers_floor():
        snowflake_coordinate_list_x.pop(i)
        snowflake_coordinate_list_y.pop(i)


