# Разбор ДЗ
"""Задача 10 (по желанию). Снова палиндром
Пользователь вводит строку. Необходимо написать программу, которая определяет,
существует ли у этой строки такая перестановка, при которой она станет палиндромом.
Выведите соответствующее сообщение.
Пример 1:
Введите строку: aab
Можно сделать палиндромом

Пример 2:
Введите строку: aabc
Нельзя сделать палиндромом
"""


def is_poly(string):
    char_dict = {}
    # Заполнение словаря char_dict в формате (символ: количество таких символов в строке)
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    # Подсчет количества нечетных значений символов в строке/словаре
    odd_count = 0  # odd - нечетный
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


my_string = input('Введите строку: ')
if is_poly(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
