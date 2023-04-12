# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
if envelop_x >= paper_x and envelop_y >= paper_y:
    print('ДА')
else:
    print('НЕТ')


# Листик же можно перевернуть. Вот этот, например # paper_x, paper_y = 6, 8



# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x1, brick_y1, brick_z = 11, 10, 2
brick_x2, brick_y2, brick_z = 11, 2, 10
brick_x3, brick_y3, brick_z = 10, 11, 2
brick_x4, brick_y4, brick_z = 10, 2, 11
brick_x5, brick_y5, brick_z = 2, 10, 11
brick_x6, brick_y6, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)
if hole_x >= brick_x1 and hole_y >= brick_y1:
    print('ДА')
elif hole_x >= brick_x2 and hole_y >= brick_y2:
    print('ДА')
elif hole_x >= brick_x3 and hole_y >= brick_y3:
    print('ДА')
elif hole_x >= brick_x4 and hole_y >= brick_y4:
    print('ДА')
elif hole_x >= brick_x5 and hole_y >= brick_y5:
    print('ДА')
elif hole_x >= brick_x6 and hole_y >= brick_y6:
    print('ДА')
else:
    print('НЕТ')
# TODO здесь ваш код

#  Тут можно в отдельные переменные присваивать два минимальных размера кирпича и сравнивать их с размерами дыры
# Что бы наверняка не ошибиться, можно их(размеры) сортирвать. Например Х самый маленький, Y второй по размеру.
# И так же смотреть чтобы размеры дыры шли в таком же порядке.  
