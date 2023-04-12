# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
thirty_one = [1, 3, 5, 7, 8, 10, 12]

if 1 <= month <= 12:
    if month in thirty_one:
        days_in_month = 31
        print(days_in_month)
    elif month == 2:
        days_in_month = 28
        print(days_in_month)
    else:
        days_in_month = 30
        print(days_in_month)
else:
    print('Такого месяца не существует')

# Ok
