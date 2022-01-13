# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
# Пропустил
# 2 ==========================================================================
# Пропустил
# 3 ==========================================================================
# string = input('Введите текст: ')
# i = 0
# for sym in string:
#     i += 1
#     if sym == '*':
#         N = i
# print("Символ '*' стоит на позиции " , N)
# 4 ==========================================================================
# a = int(input('Введите количество рядов: '))
# b = int(input('Введите количество сидений: '))
# c = int(input('Введите количество метров между рядами: '))

# print('\nСцена\n')
# for num in range(a):
#     print('=' * b, '*' * c, '=' * b)
# 5 ==========================================================================
# N = int(input('Введите число N: '))
# for num in range(N+1):
#     if num == 0:
#         print(num, end = '  ')
#     elif num % 2 != 0:
#         print(num)
#     elif num % 2 == 0:
#         print(num, end = '  ')
# 6 ==========================================================================
# x = 8
# y = 10
# while True:
#     go = input('Марсоход находится на позиции ' + str(x) + ', ' + str(y) + ' введите команду: ')
#     if go == 'a':
#         x -= 1
#     elif go == 'd':
#         x += 1
#     elif go == 'w':
#         y += 1
#     else:
#         y -= 1
#     if x == -1 or y == -1 or x == 16 or y == 21:
#         print('Марсоход уперся в стену, завершение программы ...')
#         break
# 7 ==========================================================================
# Пропустил
# 8 ==========================================================================
# text = input('Введите ФИ: ')
# name_surname = ''

# for sym in text:
#     name_surname += sym
#     if sym == ' ':
#         surname = name_surname
#         name_surname = ''
# name = name_surname

# print('Фамилия: ', surname)
# print('Имя: ', name)
# 9 ==========================================================================

# text = input('Введите текст: ')
# k = 1
# prev = ''
# maxx = 0

# for sym in text:
#     if sym == prev:
#         k += 1
#     else:
#         prev = sym
#         k = 1
#     if k > maxx:
#         maxx = k

# print('Самая длинная последовательность: ', maxx)

# 10 ==========================================================================

# text = input('Введите текст: ')
# text = text + ' '
# i = 0
# k = 0
# sym_word_1 = 0

# for sym in text:
#     i += 1
#     if sym == ' ':
#         k += 1
#         sym_word_2 = i - 1
#         print('Длина', k, '- го слова: ', sym_word_2)
#         if sym_word_2 < sym_word_1:
#             maxx = sym_word_1
#         else:
#             maxx = sym_word_2

#         i = 0

# print('Длина самого длинного слова: ', maxx)

# 11 ==========================================================================

# num_sym = 0
# text = input('Введите слово: ')

# for sym in text:
#     num_sym += 1
#     if num_sym == 1:
#         first_sym = sym
#         print('Первая буква слова: ', first_sym)
# print('Последняя буква слова: ', sym)

# if first_sym == sym:
#     print('Первая и последняя буквы одинаковые')
# else:
#     print('Первая и последняя буквы разные')

# 12 ==========================================================================

# footers = int(input('Введите общую длину колонтитула : '))         # footers - колонтитулы
# exclamation_point = int(input('Введите желаемое количество восклицательных знаков: '))       # exclamation_point - восклицательный знак
# a = int((footers - exclamation_point)/2)

# if footers > exclamation_point:
#     print('~' * a, end = '')
#     print('!' * exclamation_point, end = '')
#     print('~' * a)
# else:
#     print('Общая длина колонтитула не может быть меньше количества восклицательных знаков!')

# 13 ==========================================================================

# milk = 0
# total_milk = 0
# i = 0

# string = input('Введите текст: ')
# for symbol in string:
#     i += 1
#     milk += 2
#     if symbol == 'b':
#         total_milk += milk
#         print('В', i,'- ом стойле, произведено молока: ', milk)
#     else:
#         print('В', i,'- ом стойле, коров нет')
# print('В итоге за день произведено молока: ', total_milk)

# 14 ==========================================================================

# word_num = 1
# sym_num = 0
# sym_2_num = 0

# string = input('Введите текст: ')
# for sym in string:
#     if sym == ' ':
#         word_num += 1
#     else:
#         sym_2_num += 1
#     sym_num += 1

# print('Количество слов: ', word_num)
# print('Количество символов (с пробелами): ', sym_num)
# print('Количество символов (без пробелов): ', sym_2_num)

# 15.1 ==========================================================================
# print('==================================')
# text = 'shacnidw'
# text = 'iolidra'
# i = 1
# j = 0
# N = 0
# k = 0
# word_1, word_2, word_3 = '', '', ''

# for sym in text:
#     if i % 2 != 0: 
#         word_1 += sym
#     elif i % 2 == 0:
#         word_2 += sym
#         N += 1
#     i += 1

# while j < N:
#     k = 0
#     for sym in word_2:
#         k += 1
#         if k == N - j:
#             word_3 += sym
#     j += 1

# print('Расшифрованное сообщение: ', word_1 + word_3, end = '')
# 15.2 ==========================================================================
# print('==================================')
# text = 'shacnidw'
# text = 'iolidra'
# i = 1
# N = 0
# k = 0

# word_1, word_2, word_3 = '', '', ''

# for sym in text:
#     if i % 2 != 0: 
#         word_1 += sym
#     elif i % 2 == 0:
#         word_2 += sym
#         N += 1
#     i += 1

# for j in range(0, N):
#     k = 0
#     for sym in word_2:
#         k += 1
#         if k == N - j:
#             word_3 += sym

# print('Расшифрованное сообщение: ', word_1 + word_3, end = '')

# 15.3 ==========================================================================

text = 'shacnidw'
# text = 'iolidra'
i = 1
N = 0
k = 0
a, b, c, d, e, f = '', '', '', '', '', ''

word_1, word_2, word_3 = '', '', ''

for sym in text:
    if i % 2 != 0: 
        word_1 += sym
    elif i % 2 == 0:
        word_2 += sym
        N += 1
    i += 1

for sym in word_2:
    k += 1
    if k == 1:
        a = sym
    elif k == 2:
        b = sym
    elif k == 3:
        c = sym
    elif k == 4:
        d = sym
    elif k == 5:
        e = sym
    elif k == 6:
        f = sym
word_2 = f + e + d +c + b + a

print('Расшифрованное сообщение: ', word_1 + word_2, end = '')