# Home Work
# 1 ==========================================================================
# for row in range(6):
#     for col in range(0, 12, 2):
#         print(col+row, end = '\t')
#     print()
# 2 ==========================================================================
# N = int(input('Введите число N: '))
# for row in range(1, N + 1):
#     for col in range(1, N + 1):
#         if row == col:
#             print(row, end = ' ')
#         elif col < row:
#             print(row, end = ' ')
#         else:
#             print(end = ' ')
#     print()
# 3 ==========================================================================
# for row in range(1, 21):
#     for col in range(1, 51):
#         if col == 50/2:
#             if row == 1:
#                 print('^', end = '')
#             elif row == 20/2:
#                 print('+', end = '')
#             else:
#                 print('|', end = '')
#         elif row == 20/2:
#             if col == 50:
#                 print('>', end = '')
#             else:
#                 print('-', end = '')
#         else:
#             print(' ', end = '')
#     print()
# 4 ==========================================================================
# width = int(input('Введите ширину рамки в символах: '))     # width - ширина
# height = int(input('Введите высоту рамки в символах: '))    # height - высота
# for row in range(height + 1):
#     for col in range(width + 1):
#         if col == 0 or col == width:
#             print('|', end = '')
#         elif row == 0 or row == height:
#             print('-', end = '')
#         else:
#             print(' ', end = '')
#     print()
# 5 ==========================================================================
# N = int(input('Введите число N: '))
# for row in range(N + 1):
#     for col in range(N + 1):
#         if row == col or col == - row + N:
#             print('^', end = '')
#         else:
#             print(' ', end = '')
#     print()
# 6 ==========================================================================
# N = int(input('Введите количество чисел последовательности: '))
# count = 0
# for number in range(N):
#     isPrime = True
#     while True:
#         num = int(input(f'Введите {number + 1}-е число последовательности: '))
#         if num < 2:
#             print(f'Число последовательности не должно быть равно 1! Попробуйте еще раз...')
#         else:
#             break
#     for devider in range(2, num):
#         if num % devider == 0:
#             isPrime = False
#     if isPrime:
#         count += 1
# print('Количество простых чисел в заданной последовательности равно: ', count)
# 7 ==========================================================================
# print('====================================')
# N = int(input('Введите размер матрицы: '))
# for row in range(N):
#     for col in range(N):
#         if col == row or col == (N-1) - row:
#             print(1, end = ' ')
#         elif col < row or col > (N-1) - row:
#             print(2, end = ' ')
#         # elif col < row:
#         #     print(2, end = ' ')
#         else:
#             print(0, end = ' ')
#     print()
# print('====================================')
# 8 ==========================================================================
# print('====================================')
# start = int(input('Введите начало диапазона: '))
# stop = int(input('Введите конец диапазона: '))
# while stop < start:
#     print('Неверный диапазон! Первое число больше второго! Введите заново!')
#     start = int(input('Введите начало диапазона: '))
#     stop = int(input('Введите конец диапазона: '))
# for num in range(start, stop + 1, 1):
#     print('->', num, end = ' ')
#     while num != 1:
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = (num * 3 + 1) // 2
#         print(num, end = ' ')
#     print()
# print('====================================')
# 9 ==========================================================================
# print('====================================')
# N = int(input('Введите число N: '))
# summ = 0
# factorial = 1
# for num in range(1, N + 1):
#     factorial *= num
#     summ += factorial
# print('Сумма факториалов: ', summ)
# print('====================================')
# 10 ==========================================================================
# print('=' * 50)
# maxx = 0
# M = int(input('Введите количество чисел: '))

# for num in range(M):
#     summ = 0
#     N = int(input('Введите натуральное число: '))
#     number = N
#     while (number % 10) > 0:
#         summ += number % 10
#         number //= 10
#     if summ > maxx:
#         maxx_Num = N
#         maxx = summ
# print('Наибольшее по сумме цифр число: ', maxx_Num, '\nСумма его цифр равна: ', maxx)
# print('=' * 50)
# 11 ==========================================================================
# print('=' * 50)
# for num in range(1, 10000+1):
#     summ = 0
#     for dev in range(1, num):
#         if num % dev == 0 and num != dev:
#             summ += dev
#     if summ == num:
#         print(f'Число {num} - | совершенное | :)')
#     # else:
#     #     print(f'Число {num} - НЕ совершенное  :(')
# print('=' * 50)
# 12 ==========================================================================
# print('=' * 50)
# name = input('Введите Ваше имя: ')
# countName = 0
# for quant in name:
#     countName += 1
# print('|' + '-'* countName + '|')
# print('|' + name + '|')
# print('|' + '-'* countName + '|')
# print('=' * 50)
# 13 ==========================================================================

# height = int(input('Введите высоту пирамиды: '))    # height - высота
# Вар 1 
# for symNum in range(1, 2 * height, 2):
#     print(' ' * (((2 * height - 1) - symNum) // 2), '#' * symNum)
# # Вар 2
# for symNum in range(1, (1 + 2 * (height - 1)) + 1, 2):    # арифметическая прогрессия
#     print(' ' * (((1 + 2 * (height - 1)) - symNum)//2), '#' * symNum)
# # Вар 3
# quant = 1
# for space in range(height - 1, -1, -1):
#     print(' ' * space, '#' * quant)
#     quant += 2
# Вар 4
# for num in range(1, 2*height, 2):
#     print(' ' * (((2 * height - 1) - num) // 2), end = '')
#     for symNum in range(num):
#         print('#', end = '')
#     print()
# Вар 5
# height = int(input('Введите высоту пирамиды: '))    # height - высота
# width = 1 +  (height - 1) * 2   # width - ширина
# for row in range(height):
#     for col in range(width):
#         if col > row + (height - 1) or col < -row + (height - 1):
#             print(' ', end = '')
#         else:
#             print('#', end = '')
#     print()
# 14 ==========================================================================
# level = int(input('Введите кол-во уровней пирамиды: '))    # height - высота
# num = 1
# N = level - 1
# for row in range(level):
#     print((N-row) * '---', end = '')
#     for col in range(row + 1):
#         print(num, end = '    ')
#         num = num + 2
#     print()
# 15 ==========================================================================
# print('=' * 50)

# N = int(input())
# countSym = 2*N - 2
# start = N

# for row in range(1, N+1):
#     for sym_left in range(row):
#         print(N - sym_left, end = '')
#     print('.' * countSym, end = '')
#     for sym_right in range(start, (N - 1), -1):
#         symbol = 2 * N - sym_right
#         print(symbol, end = '')
#     print()
#     start += 1
#     countSym -= 2

# print('=' * 50)
# 16.1 ==========================================================================
# lines = int(input('Сколько уровней пирамиды паскаля отобразить? '))

# for n in range(lines):
#     Cnk = 1
#     space = lines - n - 1
#     print('-' * space, Cnk, end = '-')
#     for k in range(1, n + 1):
#         Cnk = Cnk * (n - k + 1) // k
#         print(Cnk, end = '-')
#     print()
# 16.2 ==========================================================================
# lines = int(input('Сколько уровней пирамиды паскаля отобразить? '))
# string = ''
# symbol = '1'
# space = ' '

# for n in range(lines):
#     print(' ' * (lines - 1 - n), end = '')
#     if n <= 1:
#         string += symbol + space
#     else:
#         summ = 0
#         nextt_line = ''
#         current_sym = ''
#         for sym in string:
#             if sym != ' ':
#                 current_sym += sym
#             else:
#                 summ = summ + int(current_sym)
#                 nextt_line += str(summ) + space
#                 summ = int(current_sym)
#                 current_sym = ''
#         nextt_line += str(summ)
#         string = nextt_line + space
#     print(string)
# 16.3 ====================================================
# Вариант 16.3 корректно выводит треугольник Паскаля только до 6 строчки, т.к. этот 
# алгоритм дальше не справляется

# lines = int(input('Сколько уровней пирамиды паскаля отобразить? '))
# lines = lines - 2
# flag = 0

# symbols = 11
# if lines >= 5:
#     print('=' * 65)
#     print('Этот алгоритм выводит треугольник Паскаля только до 6 строчки!')
#     print('=' * 65)
# elif lines == -1:
#     print(1)
# elif lines == 0:
#     print('', 1)
#     print(1, 1)
# else:
#     for n in range(lines):
#         if flag == 0:
#             print(' ' * (lines - n), 1)
#             print(' ' * (lines - 1 - n), 1, 1)
#             flag = 1
#         print(' ' * (lines - 1 - n), end = '')
#         count = symbols
#         coef = 1
#         while count != 0:
#             count //= 10
#             coef *= 10
#         summ = 0
#         nextt_sym = 0
#         while symbols != 0:
#             last_sym = symbols % 10
#             summ = summ + last_sym
#             print(summ, end = ' ')
#             nextt_sym = nextt_sym + summ * coef
#             coef //= 10
#             summ = last_sym
#             symbols = symbols // 10
#         nextt_sym += last_sym
#         symbols = nextt_sym
#         print(last_sym)




# lines = int(input('Сколько уровней пирамиды паскаля отобразить? '))
# lines = lines - 2

# symbols = 11
# print(1)
# print(1, 1)
# for n in range(lines):
#     count = symbols
#     coef = 1
#     while count != 0:
#         count //= 10
#         coef *= 10
#     summ = 0
#     nextt_sym = 0
#     while symbols != 0:
#         last_sym = symbols % 10
#         summ = summ + last_sym
#         print(summ, end = ' ')
#         nextt_sym = nextt_sym + summ * coef
#         coef //= 10
#         summ = last_sym
#         symbols = symbols // 10
#     nextt_sym += last_sym
#     symbols = nextt_sym
#     print(last_sym)