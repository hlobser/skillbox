# -*- coding: utf-8 -*-
import os
from pprint import pprint
from threading import Thread, Lock

# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле

def print_volatility(volatility_summ_dict):
    zero_vol = '     '
    print(len(volatility_summ_dict))
    for ticker_number, volatility in volatility_summ_dict.copy().items():
        if volatility == 0:
            volatility_summ_dict.pop(ticker_number)
            zero_vol += f' ТИКЕР_{ticker_number},'
    zero_vol = zero_vol.rstrip(',')
    sorted_vol = sorted(volatility_summ_dict.items(), key=lambda x: x[1], reverse=True)
    print('  Максимальная волатильность:')
    for ticker_number, volatility in sorted_vol[:3]:
        print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
    print('  Минимальная волатильность:')
    for ticker_number, volatility in sorted_vol[-3:]:
        print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
    print('  Нулевая волатильность:')
    print(zero_vol)

def get_full_path(folder_to_scan):
    full_path_list = []
    path = os.path.abspath(folder_to_scan)
    for dirpath, _, filename_list in os.walk(path):
        for filename in filename_list:
            full_path = os.path.join(dirpath, filename)
            full_path_list.append(full_path)
    return full_path_list

def chuncs(row, n):
    res = []
    for elem in row:
        if res and len(res[-1]) != n:
            res[-1].append(elem)
        else:
            res.append([elem])
    return res

class TradeParser(Thread):


    def __init__(self, path, lock, volatility_summ_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.volatility_dict = dict()
        self.lock = lock
        self.volatility_summ_dict = volatility_summ_dict

    def run(self):
        self._find_volatility()
        with self.lock:
            self.volatility_summ_dict.update(self.volatility_dict)

    def _find_volatility(self):
        for path1 in self.path:
            with open(file=path1) as file:
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
                # with self.lock:
                self.volatility_dict[ticker_num] = volatility





path_list = get_full_path(folder_to_scan='trades')
path_chunked_4 = chuncs(path_list, 28)

volatility_summ_dict = dict()
lock = Lock()

trades = [TradeParser(path=path, volatility_summ_dict=volatility_summ_dict, lock=lock) for path in path_chunked_4]
for trade in trades:
    trade.start()
for trade in trades:
    trade.join()
print_volatility(volatility_summ_dict)


