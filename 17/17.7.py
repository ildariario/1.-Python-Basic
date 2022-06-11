# Home Work
# 1 ==========================================================================
'''Задача 1. Гласные буквы
Команде лингвистов понравилось качество ваших программ, и они решили заказать у вас
функцию для анализатора текста, которая создавала бы список гласных букв текста, а
заодно считала бы их количество.
Напишите программу, которая запрашивает у пользователя текст и генерирует список из
гласных букв этого текста (сама строка вводится на русском языке). Выведите в консоль
сам список и его длину.

Пример:
Введите текст: Нужно отнести кольцо в Мордор!

Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
Длина списка: 9
'''
# Пропустил
# 2 ==========================================================================
'''Задача 2. Генерация
Пользователь вводит целое число N. Напишите программу, которая генерирует список из N 
чисел, на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от 
деления своего номера на 5.

Пример:
Введите длину списка: 10
Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Случайные соревнования
Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований. 
Есть два списка (то есть две команды), по 20 участников в каждом. В этих списках хранятся 
очки каждого участника (это вещественные числа с двумя знаками после точки, например 4.03). 
Участник одной команды соревнуется с участником другой команды под таким же номером. То есть 
первый соревнуется с первым, второй — со вторым и так далее.
Напишите программу, которая генерирует два списка участников (по 20 элементов) из случайных 
вещественных чисел (от 5 до 10). Для этого найдите подходящую функцию из модуля random. 
Затем сгенерируйте третий список, в котором окажутся только победители из каждой пары.

Пример:
Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
'''
# Пропустил
# 4 ==========================================================================
'''Задача 4. Тренируемся со срезами
Дана строка, в которой хранятся первые семь букв английского алфавита. 
alphabet = 'abcdefg'
Напишите программу, которая выводит на экран 10 вот таких результатов:
1.	Копия строки.
2.	Элементы строки в обратном порядке.
3.	Каждый второй элемент строки (включая самый первый).
4.	Каждый второй элемент строки после первого.
5.	Все элементы до второго.
6.	Все элементы, начиная с конца до предпоследнего.
7.	Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
8.	Последние три элемента строки.
9.	Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
10.	То же, что и в предыдущем пункте, но в обратном порядке.
Для получения и вывода результатов используйте только команду print и срезы.

Результаты работы программы:

1: abcdefg
2: gfedcba
3: aceg
4: bdf
5: a
6: g
7: d
8: efg
9: de
10: ed
'''
# alphabet = 'abcdefg'
# copy_list = alphabet[:]
#
# print('1.', copy_list)             # 1.	  Копия строки.
# print('2.', copy_list[::-1])       # 2.	  Элементы строки в обратном порядке.
# print('3.', copy_list[::2])        # 3.	  Каждый второй элемент строки (включая самый первый).
# print('4.', copy_list[1::2])       # 4.	  Каждый второй элемент строки после первого.
# print('5.', copy_list[:1])         # 5.	  Все элементы до второго.
# print('6.1.', copy_list[:-7:-1])   # 6.	  Все элементы, начиная с конца до предпоследнего (с конца).
# print('6.2.', copy_list[:0:-1])    # 6.1. Все элементы, начиная с конца до предпоследнего (с конца).
# print('6.3.', copy_list[:-2:-1])   # 6.2. Все элементы, начиная с конца до предпоследнего (сначала).
# print('7.', copy_list[3:4])        # 7.	  Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
# print('8.', copy_list[4:])         # 8.	  Последние три элемента строки.
# print('9.', copy_list[3:5])        # 9.	  Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
# print('10.1.', copy_list[-3:-5:-1])  # 10.1.То же, что и в предыдущем пункте, но в обратном порядке.
# print('10.2.', copy_list[-3:2:-1])   # 10.2.То же, что и в предыдущем пункте, но в обратном порядке.
# 5 ==========================================================================
'''Задача 5. Разворот
На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. 
Реализуйте код, который разворачивает последовательность символов, заключённую между первым 
и последним появлением буквы h, в противоположном порядке.
'''
# string = 'abc-h-def-h-g-h-ijklm'
# string = string[string.index('h') + 1:]
# string = string[::-1]
# string = string[string.index('h') + 1:]
# print(string)
# 6 ==========================================================================
'''Задача 6. Сжатие списка
Дан список из N целых чисел. Напишите программу, которая выполняет «сжатие списка» — 
переставляет все нулевые элементы в конец массива. При этом все ненулевые элементы 
располагаются в начале массива в том же порядке. Затем все нули из списка удаляются.
'''
# import random
#
# N = random.randint(5, 10)
# list_1 = [random.randint(0, 10) for _ in range(N)]
# # list_1 = [1, 0, 2, 3, 0, 4, 5, 0, 6, 0, 7]
# print(list_1)
# if list_1.count(0) != 0:
#     for i in range(list_1.count(0)):
#         list_1.remove(0)
#         list_1.append(0)
#     list_1 = list_1[:-i-1]
#     print(list_1)
# else:
#     print('В исходном списке нулевых элементов нет!')
# 7 ==========================================================================
'''Задача 7. Двумерный список
Как мы говорили ранее, в программировании часто приходится писать код исходя из 
результата, который требует заказчик. В этот раз заказчику нужно получить вот такой 
двумерный список:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Напишите программу, которая генерирует такой список и выводит его на экран. Используйте 
только list comprehensions.
'''
# # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# total_list = [[x for x in range(1, 13, 4)], [x for x in range(2, 13, 4)],
#               [x for x in range(3, 13, 4)], [x for x in range(4, 13, 4)]]
#
# # total_list = []
# # for i_start in range(1, 5):
# #     total_list.append([x for x in range(i_start, 13, 4)])
#
# print(total_list)
# 8 ==========================================================================
'''Задача 8. Развлечение
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем 
по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i 
до R_i включительно. Определите, какие палки остались стоять на месте.
Напишите программу, которая получает на вход количество палок N и количество бросков K. 
Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N.
Программа должна вывести последовательность из N символов, где j-й символ есть “I”, 
если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

Пример:
Кол-во палок: 10 
Кол-во бросков: 3
Бросок 1. Сбиты палки с номера 8 
по номер 10
Бросок 2. Сбиты палки с номера 2 
по номер 5
Бросок 3. Сбиты палки с номера 3 
по номер 6

Результат: I.....I...
'''
# import random
#
# N = int(input('Кол-во палок: '))
# K = int(input('Кол-во бросков: '))
#
# stick_status = [1 for _ in range(N)]
#
# print('Положение палок до броска:', stick_status)
#
# for i_shot in range(K):
#     R_i = random.randint(1, N)
#     L_i = random.randint(1, R_i)
#     print('\nБросок', i_shot + 1, '. Сбиты палки с номера', L_i, 'по номер', R_i)
#     stick_status[L_i - 1:R_i] = [0 for _ in range(len(stick_status[L_i - 1:R_i]))]
#     print('Текущее положение палок:  ', stick_status)
#
# print('\nРезультат:')
# for i_stick in stick_status:
#     if i_stick == 1:
#         print('I', end='')
#     else:
#         print('.', end='')
# 9 ==========================================================================
'''Задача 9. Список списков
Дан вот такой (уже многомерный!) список:
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список.
Для решения используйте только list comprehensions. 
Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
'''
# nice_list = [1, 2, 3, 4, 5, 6]
# output = [digit for digit in nice_list]
# print(output)

# nice_list = [[1, 2], [3, 4], [5, 6]]
# output = [digit for each_list in nice_list for digit in each_list]
# print(output)

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# output = [digit for each_list_1 in nice_list for each_list_2 in each_list_1 for digit in each_list_2]
# print(output)
# 10 ==========================================================================
'''Задача 10. Шифр Цезаря (сделайте по желанию)
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на 
следующую по алфавиту через K позиций по кругу. Если взять русский алфавит и k = 3, 
то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая 
зашифрует это сообщение при помощи шифра Цезаря.
Пример:
Введите сообщение: это питон
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср
'''
def caesar_cipher(string, user_shift):
    print(alphabet)
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)

print('Зашифрованная строка:', output_str)
