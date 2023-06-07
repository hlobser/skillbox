# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
# TODO здесь ваш код

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def error_checking(line):
    if len(line) < 3:
        raise ValueError('Одно из полей не заполнено')
    elif not line[0].isalpha():
        raise NotNameError('В поле "имя" содержатся недопустимые символы')
    elif '@' not in line[1] and '.' not in line[1]:
        raise NotEmailError('Неправильный email')
    elif not 10 <= int(line[2]) <= 99:
        raise ValueError('Возраст вне диапазона')


with open(file='registrations.txt', mode='r', encoding='utf8') as file:
    for line_1 in file:
        line = line_1.split()
        try:
            error_checking(line)
        except Exception as exc:
            with open(file='registrations_bad.log', mode='a', encoding='utf8') as f_bad:
                f_bad.write(f'{line_1[:-1]},  {exc} \n')
                continue
        with open(file='registrations_good.log', mode='a', encoding='utf8') as f_good:
            f_good.write(line_1)
