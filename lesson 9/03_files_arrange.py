# -*- coding: utf-8 -*-

import os, time, shutil

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
class SortingPhotos():

    def __init__(self, folder_to_scan='icons', target_folder='icons_by_year'):
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
                    self._copy_file()

    def _get_photo_info(self):
        time_sec = os.path.getctime(self.full_path)
        time_utc = time.gmtime(time_sec)
        self.year = time_utc[0]
        self.month = time_utc[1]

    def _create_folders(self):
        os.makedirs(f'{self.target_folder}\\{self.year}\\{self.month}', exist_ok=True)

    def _copy_file(self):
        shutil.copy2(self.full_path, f'{self.target_folder}\\{self.year}\\{self.month}')

    # def replace_file(self):
    #     os.replace(self.full_path, os.path.join(f'{self.target_folder}\\{self.year}\\{self.month}', self.filename))


copy_photos = SortingPhotos()
copy_photos.sorting()




# path = os.path.abspath('icons')
# for dirpath, _, filename_list in os.walk(path):
#     if filename_list:
#         for filename in filename_list:
#             full_path = os.path.join(dirpath, filename)
#             time_sec = os.path.getctime(full_path)
#             time_utc = time.gmtime(time_sec)
#             year = time_utc[0]
#             month = time_utc[1]
#             # os.makedirs(f'icons_by_year\\{year}\\{month}', exist_ok=True)
#             # shutil.copy2(full_path, f'icons_by_year\\{year}\\{month}')
#             os.remove(f'icons_by_year\\{year}\\{month}\\{filename}')
#         os.removedirs(f'icons_by_year\\{year}\\{month}')



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# path = os.path.abspath('address-book-new.png')
# os.makedirs('a', exist_ok=True)
# shutil.copy2(path, 'a\\address-book-new.png')
# os.remove('a\\address-book-new.png')
# os.rmdir('a')                               #удалить директорий
# os.replace(path, 'a\\address-book-new.png')