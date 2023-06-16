# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# TODO здесь ваш код
def log_parser():
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
                        yield prev_date + ']', str(count)
                    minute_prev_line = minute_this_line
                    prev_date = date
                    count = 0
                    if 'NOK' in event:
                        count += 1


grouped_events = log_parser()
for group_time, event_count in grouped_events:
    print(f'{group_time} {event_count}')
