# -*- coding: utf-8 -*-
import os


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле
class TradeParser():

    def __init__(self, folder_to_scan):
        self.folder_to_scan = folder_to_scan
        self.full_path_list = []
        self.volatility_dict = dict()

    def run(self):
        self._get_full_path()
        self._find_volatility()
        self._print_volatility()

    def _get_full_path(self):
        path = os.path.abspath(self.folder_to_scan)
        for dirpath, _, filename_list in os.walk(path):
            for filename in filename_list:
                full_path = os.path.join(dirpath, filename)
                self.full_path_list.append(full_path)

    def _find_volatility(self):
        for path in self.full_path_list:
            with open(file=path) as file:
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

    def _print_volatility(self):
        zero_vol = '     '
        for ticker_number, volatility in self.volatility_dict.copy().items():
            if volatility == 0:
                self.volatility_dict.pop(ticker_number)
                zero_vol += f' ТИКЕР_{ticker_number},'
        zero_vol = zero_vol.rstrip(',')
        sorted_vol = sorted(self.volatility_dict.items(), key=lambda x: x[1], reverse=True)
        print('  Максимальная волатильность:')
        for ticker_number, volatility in sorted_vol[:3]:
            print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
        print('  Минимальная волатильность:')
        for ticker_number, volatility in sorted_vol[-3:]:
            print(f'      ТИКЕР_{ticker_number} - {volatility:.2f} %')
        print('  Нулевая волатильность:')
        print(zero_vol)


trade = TradeParser(folder_to_scan='trades')
trade.run()
