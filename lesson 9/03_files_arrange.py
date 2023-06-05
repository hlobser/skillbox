# -*- coding: utf-8 -*-

import os, time, shutil
from abc import abstractmethod, ABCMeta


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
class MovingPhotos(metaclass=ABCMeta): # родительский класс

    def __init__(self, folder_to_scan, target_folder):
        self.folder_to_scan = folder_to_scan
        self.target_folder = target_folder

    def sorting(self):
        path = os.path.abspath(self.folder_to_scan)
        for dirpath, _, filename_list in os.walk(path):
            if filename_list:
                for self.filename in filename_list:
                    self.full_path = os.path.join(dirpath, self.filename)
                    self._get_photo_info()
                    self._create_folders()
                    self._replace_file()
        self._delete_empty_folders()

    def _get_photo_info(self):
        time_sec = os.path.getctime(self.full_path)
        time_utc = time.gmtime(time_sec)
        self.year = str(time_utc[0])
        self.month = str(time_utc[1])

    @abstractmethod
    def _create_folders(self):
        pass

    @abstractmethod
    def _replace_file(self):
        pass

    @abstractmethod
    def _delete_empty_folders(self):
        pass


class ReplacePhotosForDate(MovingPhotos):

    def _create_folders(self):
        os.makedirs(os.path.join(self.target_folder, self.year, self.month), exist_ok=True)

    def _replace_file(self):
        os.replace(self.full_path, os.path.join(self.target_folder, self.year, self.month, self.filename))

    def _delete_empty_folders(self):
        shutil.rmtree(self.folder_to_scan)



class ReplacePhotosInHeap(MovingPhotos):

    def _create_folders(self):
        os.makedirs(self.target_folder, exist_ok=True)

    def _replace_file(self):
        os.replace(self.full_path, os.path.join(self.target_folder, self.filename))

    def _delete_empty_folders(self):
        shutil.rmtree(os.path.join(self.folder_to_scan))


# sort_by_date = ReplacePhotosForDate(folder_to_scan='icons', target_folder='icons_by_year')
# sort_by_date.sorting()

sort_in_heap = ReplacePhotosInHeap(folder_to_scan='icons_by_year', target_folder='icons')
sort_in_heap.sorting()






# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
