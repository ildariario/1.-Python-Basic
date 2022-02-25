# Task 1


# Task 2


# Task 3


# Home Work
# 1 ==========================================================================

# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================
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
# string = 'abc-h-def-h-g-h-ijklm'
# string = string[string.index('h') + 1:]
# string = string[::-1]
# string = string[string.index('h') + 1:]
# print(string)
# 6 ==========================================================================
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
# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
