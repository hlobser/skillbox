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
class LogParser():

    def __init__(self, filename, output_filename, sorting_key='minute'):
        self.filename = filename
        self.output_filename = output_filename
        self.count = 0
        self.sorting_key = sorting_key

    def _first_date_and_event(self):
        with open(self.filename, mode='r', encoding='utf8') as log_file:
            line = log_file.readline()
            self.sorting = {'minute': line.index(' ') + 5,
                            'hour': line.index(' ') + 2,
                            'month': line.index('-') + 2,
                            'year': line.index('-') - 1}
            self.time_prev_line = line[self.sorting[self.sorting_key]]
            self.prev_date = line[:self.sorting[self.sorting_key] + 1]

    def parse(self):
        self._first_date_and_event()
        with open(self.filename, mode='r', encoding='utf8') as log_file:
            for line in log_file:
                self.date, self.event = line[:self.sorting[self.sorting_key] + 1], line[line.index(']') + 1:]
                self.time_this_line = self.date[-1]
                self._count_events()
            if self.count:
                self._write_file()

    def _count_events(self):
        if self.time_this_line == self.time_prev_line:
            if 'NOK' in self.event:
                self.count += 1
        else:
            if self.count:
                self._write_file()
            self.time_prev_line = self.time_this_line
            self.prev_date = self.date
            self.count = 0
            if 'NOK' in self.event:
                self.count += 1

    def _write_file(self):
        with open(self.output_filename, mode='a', encoding='utf8') as count_file:
            if self.sorting_key == 'minute' or self.sorting_key == 'hour':
                text = f'{self.prev_date}:00] {str(self.count)}\n'
            elif self.sorting_key == 'month' or self.sorting_key == 'year':
                text = f'{self.prev_date}] {str(self.count)}\n'
            count_file.write(text)


parser = LogParser(filename='events.txt', output_filename='count_of_events.txt', sorting_key='minute')
parser.parse()



# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
