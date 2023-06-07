# -*- coding: utf-8 -*-
import logging
from random import randint


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

# TODO здесь ваш код


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    karma_point = randint(1, 7)
    try:
        if karma_point == 1:
            raise IamGodError('Если бог существует, то это, мать вашу, Я!!!АХАХАХАХ')
        if karma_point == 2:
            raise DrunkError('Лучшая зарядка это балтика девятка')
        if karma_point == 3:
            raise CarCrashError('Привыкни к аппарату. Не топи, блять!!!')
        if karma_point == 4:
            raise GluttonyError('Две мясных котлеты гриль, специальный соус, сыр...')
        if karma_point == 5:
            raise DepressionError('Сначала парни говорят что депрессии нет, а потом сидят целый день и смотрят в одну точку')
        if karma_point == 6:
            raise SuicideError('Ребята, смотрите, я черешня')
    except:
        random_raise = randint(1, 13)
        if random_raise == 1:
            raise
    return karma_point

# logging.basicConfig(filename="log.txt", level = logging.ERROR, encoding='utf8')
karma = 0
while karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        with open(file='log.txt', mode='a', encoding='utf8') as file:
            file.write(f'{type(exc)}: {exc}' + '\n')
        # logging.error(exc)
# https://goo.gl/JnsDqu
