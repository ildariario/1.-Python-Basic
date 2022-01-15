# Task 1

# word = input('Введите слово: ')
# replace_num = int(input('Номер символа для замены: '))
# replace_sym = input('Чем заменяем: ')
#
# sym_list = []
# for sym in word:
#     sym_list.append(sym)
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end='')

# Task 2

# word = input('Введите слово: ')
# replace_num = int(input('Номер символа для замены: '))
# replace_sym = input('Чем заменяем: ')
#
# sym_list = list(word)
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end='')

# Task 3

# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
#     print('Введите', i + 1, 'слово:', end=' ')
#     word = input()
#     words_list.append(word)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Слово из текста: ')
#
# print('\nПодсчет слов в тексте')
# for i in range(3):
#     print(words_list[i], ':', counts[i])

# Home Work
# 1 ==========================================================================
# s = input('Введите строку: ')
# list_s = list(s)
# new_list_s = []
# count = 0
#
# for sym in list_s:
#
#     if sym != ':':
#         new_list_s.append(sym)
#     else:
#         new_list_s.append(';')
#         count += 1
#
# print('Исправленная строка: ', end='')
# for i in new_list_s:
#     print(i, end='')
# print('\nКол-во замен: ', count)
# 2 ==========================================================================
# s = input('Введите строку: ')
# num_in_s = int(input('Номер символа: '))
#
# new_s = list(s)
# print(new_s)
# print('Символ слева: ', new_s[num_in_s - 2])
# print('Символ справа: ', new_s[num_in_s])
#
# if new_s[num_in_s - 2] == new_s[num_in_s - 1] and new_s[num_in_s] == new_s[num_in_s - 1]:
#     print('Есть два таких же символа.')
# elif new_s[num_in_s - 2] == new_s[num_in_s - 1] or new_s[num_in_s] == new_s[num_in_s - 1]:
#     print('Есть ровно один такой же символ.')
# else:
#     print('Таких же символов нет.')
# 3 ==========================================================================
# list_1 = []
# count = [0, 0, 0]
#
# for i in range(3):
#     print('Введите', i + 1, 'слово: ', end='')
#     word = input()
#     list_1.append(word)
#
# print(list_1)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for i in range(3):
#         if list_1[i] == text:
#             count[i] += 1
#     text = input('Слово из текста: ')
#
# print('Подсчёт слов в тексте')
# for i in range(3):
#     print(list_1[i], ':', count[i])
# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================