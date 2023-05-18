# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Ground):
            return Dirt()
        if isinstance(other, Water):
            return Water()
    def __str__(self):
        return 'Вода'


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Ground):
            return Lava()
        if isinstance(other, Fire):
            return Fire()
    def __str__(self):
        return 'Огонь'


class Ground:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Ground):
            return Ground()
    def __str__(self):
        return 'Земля'


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Ground):
            return Dust()
        if isinstance(other, Air):
            return Air()
    def __str__(self):
        return 'Воздух'


class Steam:
    def __str__(self):
        return 'Пар'


class Storm:
    def __str__(self):
        return 'Шторм'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


print(Water(), '+', Fire(), '=', Water() + Fire())
print(Ground(), '+', Water(), '=', Ground() + Water())
print(Water(), '+', Water(), '=', Water() + Water())
print(Water(), '+', Lava(), '=', Water() + Lava())
# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


