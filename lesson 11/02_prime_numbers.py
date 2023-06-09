# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.i = 0
#
#     def __iter__(self):
#         self.prime_numbers_list = self.get_prime_numbers()
#         return self
#
#     def __next__(self):
#         if self.i == len(self.prime_numbers_list):
#             raise StopIteration()
#         num = self.prime_numbers_list[self.i]
#         self.i += 1
#         return num
#
#     def get_prime_numbers(self):
#         prime_numbers = []
#         for number in range(2, self.n + 1):
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 prime_numbers.append(number)
#         return prime_numbers
#


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for number in prime_numbers_generator(n=10):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def is_lucky(number):
    num_len = len(str(number))
    # если длина числа четная, то делим число пополам, если нет, то выкидываем среднее число
    left_half, right_half = str(number)[:num_len // 2], str(number)[num_len // 2 + num_len % 2:]
    left_sum, right_sum = sum([int(i) for i in left_half]), sum([int(j) for j in right_half])
    return left_sum == right_sum


def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if is_palindrome(number) and is_lucky(number):
                yield number


for number in prime_numbers_generator(n=10000):
    print(number)
# def is_vampire():
#     pass