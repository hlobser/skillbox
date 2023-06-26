# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_, to, date):
    im = Image.open('images/ticket_template.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('ofont.ru_Kanit Cyrillic.ttf', size=15)
    y = im.size[1]
    draw.text((45, y - 275), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, y - 205), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, y - 140), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((285, y - 140), date, font=font, fill=ImageColor.colormap['black'])
    # im.show()
    im.save('ticket.png')



make_ticket(fio='Пригожин Е.В.', from_='Ростов-на-Дону', to='Минск', date='24.06')
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
