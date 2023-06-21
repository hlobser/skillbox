# -*- coding: utf-8 -*-
import os
from threading import Thread
from utils import time_track

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


class FindVolatility(Thread):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.volatility_dict = dict()

    def run(self):
        with open(file=self.path) as file:
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
            TradeParser.volatility_summ_dict.update(self.volatility_dict)


class TradeParser:
    volatility_summ_dict = {}

    def __init__(self, folder_to_scan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.folder_to_scan = folder_to_scan
        self.full_path_list = []

    def run(self):
        self._get_full_path()
        find_vol_dict = [FindVolatility(path=path) for path in self.full_path_list]
        for vol in find_vol_dict:
            vol.start()
        for vol in find_vol_dict:
            vol.join()
        self._print_volatility()

    def _print_volatility(self):
        zero_vol = '     '
        print(len(TradeParser.volatility_summ_dict))
        for ticker_number, volatility in TradeParser.volatility_summ_dict.copy().items():
            if volatility == 0:
                TradeParser.volatility_summ_dict.pop(ticker_number)
                zero_vol += f' ТИКЕР_{ticker_number},'
        zero_vol = zero_vol.rstrip(',')
        sorted_vol = sorted(TradeParser.volatility_summ_dict.items(), key=lambda x: x[1], reverse=True)
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


@time_track
def main():
    trade = TradeParser(folder_to_scan='trades')
    trade.run()


if __name__ == '__main__':
    main()



