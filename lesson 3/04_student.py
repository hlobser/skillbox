# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
educational_grant_year = 0
expenses_year = 0
i=1
while i < 10:
    expenses_year += expenses
    expenses = expenses + expenses * 0.03
    educational_grant_year += educational_grant
    i += 1
beg_parents = expenses_year - educational_grant_year
print('Cтуденту нужно попросить', round(beg_parents, 2), 'рублей')
# TODO здесь ваш код
