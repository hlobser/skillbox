# -*- coding: utf-8 -*-
import zipfile


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+

# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

class Statistic:


    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.count = 0


    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename


    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.stat[char] = self.stat.get(char, 0) + 1
                        self.count += 1

    def sorting(self):
        self.stat = dict(sorted(self.stat.items(), key=lambda x: (x[1], x[0]), reverse=True))

    def output_table(self):
        print(f'''+---------+----------+
|  буква  | частота  |
+---------+----------+''')
        for key, value in self.stat.items():
            print(f'''|    {key}    |   {value:6d}  |''')
        print(f'''+---------+----------+
|  итого  | {self.count}  |
+---------+----------+''')


stasistic = Statistic(file_name='python_snippets\\voyna-i-mir.txt.zip')
stasistic.unzip()
stasistic.collect()
stasistic.sorting()
stasistic.output_table()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
