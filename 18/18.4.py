# Task 1

# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла вместе с расширением: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if path[-4:] == '.txt':
#     print('Путь к файлу: ', path)
# else:
#     print('Ошибка: неверное расширение файла.', path)

# Task 2

# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла вместе с расширением: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if path.endswith('.txt'):
#     print('Путь к файлу: ', path)
# else:
#     print('Ошибка: неверное расширение файла.', path)

# Task 3

# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла вместе с расширением: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if path.endswith('.txt'):
#     if path.startswith('C:/')
#         print('Путь к файлу: ', path)
#     else:
#         print('Ошибка: неверно указан диск.', path)
# else:
#     print('Ошибка: неверное расширение файла.', path)

# Task 4

# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла вместе с расширением: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if path.endswith('.txt') == False:
#     print('Ошибка: неверное расширение файла.', path)
# elif path.startswith('C:/') == False:
#     print('Ошибка: неверно указан диск.', path)
# else:
#     print('Путь к файлу: ', path)

# Task 5

# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла вместе с расширением: ')
#
# path = 'C:/{user}/docs/folder/{new_file}'.format(
#     user=user_name,
#     new_file=file_name
# )
#
# if not path.endswith('.txt'):
#     print('Ошибка: неверное расширение файла.', path)
# elif not path.startswith('C:/'):
#     print('Ошибка: неверно указан диск.', path)
# else:
#     print('Путь к файлу: ', path)

# Task 6

# words_list = []
#
# for i_num in range(3):
#     print('Введите', i_num + 1, 'слово:', end=' ')
#     word = input().lower()
#     words_list.append(word)
#
# text = input('Введите текст: ').lower().split()
#
# print('\nПодсчет слов в тексте')
# for index in range(3):
#     print(words_list[index], ':', text.count(words_list[index]))

# Task 7

# words_list = []
#
# for i_num in range(3):
#     print('Введите', i_num + 1, 'слово:', end=' ')
#     word = input().upper()
#     words_list.append(word)
#
# text = input('Введите текст: ').upper().split()
#
# print('\nПодсчет слов в тексте')
# for index in range(3):
#     print(words_list[index], ':', text.count(words_list[index]))

# Home Work
# 1 ==========================================================================
# def caesar_cipher(string, user_shift):
#     char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ')
#         for sym in string
#     ]
#     new_str = ''.join(char_list)
#     return new_str
#
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# input_str = input('Введите строку: ').lower()
# shift = int(input('Введите сдвиг: '))
#
# output_str = caesar_cipher(input_str, shift)
#
# print('Зашифрованная строка:', output_str)
# 2 ==========================================================================
# path = input('Путь к файлу: ')
# disk = input('На каком диске должен лежать файл: ')
# file_ext = input('Требуемое расширение файла: ')
#
# if not path.startswith(disk):
#     print('Ошибка: Указан неверно диск!')
# elif not path.endswith(file_ext):
#     print('Ошибка: Неверное расширение файла!')
# else:
#     print('Путь корректен!')
# 3 ==========================================================================
string = input('Введите строку: ')

sym_low = len([sym for sym in string if sym.islower() == True])
sym_up = len([sym for sym in string if sym.isupper()])

if sym_up > sym_low:
    string = string.upper()
else:
    string = string.lower()
print('Результат: ', string)
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
