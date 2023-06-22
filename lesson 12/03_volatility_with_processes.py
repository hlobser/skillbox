# -*- coding: utf-8 -*-
import os
from multiprocessing import Process, Queue

from utils import time_track


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле

class FindVolatility(Process):
    def __init__(self, path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.volatility_dict = dict()
        self.collector = collector

    def run(self):
        for path_1 in self.path:
            with open(file=path_1) as file:
                file.readline()  # первую линию в файле пропускаем
                ticker_num, _, max_price, _ = file.readline().split(',')
                max_price, min_price = float(max_price), float(max_price)
                for line in file.readlines():
                    s = line.split(',')
                    price = float(s[2])
                    if price > max_price:
                        max_price = price
                    if price < min_price:
                        min_price = price
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100
                self.volatility_dict[ticker_num] = volatility
                self.collector.put(self.volatility_dict.copy())


class ProcessParser:
    volatility_summ_dict = {}
    collector = Queue()

    def __init__(self, folder_to_scan):
        self.folder_to_scan = folder_to_scan
        self.full_path_list = []

    def run(self):
        self._get_full_path()
        find_vol_dict = [FindVolatility(path=path, collector=ProcessParser.collector) for path in self.split_process()]
        for vol in find_vol_dict:
            vol.start()
        for vol in find_vol_dict:
            vol.join()
        while not ProcessParser.collector.empty():
            volatility_dict = ProcessParser.collector.get()
            ProcessParser.volatility_summ_dict.update(volatility_dict)
        self._print_volatility()

    def _print_volatility(self):
        zero_vol = '     '
        print(len(ProcessParser.volatility_summ_dict))
        for ticker_number, volatility in ProcessParser.volatility_summ_dict.copy().items():
            if volatility == 0:
                ProcessParser.volatility_summ_dict.pop(ticker_number)
                zero_vol += f' ТИКЕР_{ticker_number},'
        zero_vol = zero_vol.rstrip(',')
        sorted_vol = sorted(ProcessParser.volatility_summ_dict.items(), key=lambda x: x[1], reverse=True)
        print('  Максимальная волатильность:')
        for ticker_number, volatility in sorted_vol[:3]:
            print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
        print('  Минимальная волатильность:')
        for ticker_number, volatility in sorted_vol[-3:]:
            print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
        print('  Нулевая волатильность:')
        print(zero_vol)

    def _get_full_path(self):
        path = os.path.abspath(self.folder_to_scan)
        for dirpath, _, filename_list in os.walk(path):
            for filename in filename_list:
                full_path = os.path.join(dirpath, filename)
                self.full_path_list.append(full_path)

    def split_process(self, num_of_process=6):  # num_of_process максимум 6
        splited_path = []
        for elem in self.full_path_list:
            if splited_path and len(splited_path[-1]) != num_of_process:
                splited_path[-1].append(elem)
            else:
                splited_path.append([elem])
        return splited_path


@time_track
def main():
    trade = ProcessParser(folder_to_scan='trades')
    trade.run()


if __name__ == '__main__':
    main()

