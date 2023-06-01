# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
with open('events.txt', mode='r', encoding='utf8') as log_file:
    minute_prev_line = None
    prev_date = None
    count = 0
    for line in log_file:
        date, event = line[:line.index(' ') + 6], line[line.index(']')+1:]
        minute_this_line = date[-1]
        if minute_prev_line is None and prev_date is None:
            minute_prev_line = minute_this_line
            prev_date = date
            if 'NOK' in event:
                count += 1
        else:
            if minute_this_line == minute_prev_line:
                if 'NOK' in event:
                    count += 1
            else:
                if count:
                    with open('count_of_events.txt', mode='a', encoding='utf8') as count_file:
                        text = f'{date}] {str(count)}\n'
                        count_file.write(text)
                minute_prev_line = minute_this_line
                prev_date = date
                count = 0
                if 'NOK' in event:
                    count += 1

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
