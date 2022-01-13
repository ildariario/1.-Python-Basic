# Task 1


# Task 2


# Task 3


# Home Work
# 1 ==========================================================================
# import platform
# import sys
#
# info = 'OS info is \n{}\n\nPython version is {} {}'.format(
#     platform.uname(),
#     sys.version,
#     platform.architecture(),
# )
#
# print(info)
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#     file.write(info)
# 2 ==========================================================================
# print("Введите первую точку")
# x1 = float(input('X1: '))
# y1 = float(input('Y1: '))
#
# print("\nВведите вторую точку")
# x2 = float(input('X2: '))
# y2 = float(input('Y2: '))
#
# x_diff = x1 - x2
# y_diff = y1 - y2
#
# if x_diff == 0:
#     print("Уравнение прямой, проходящей через эти точки:")
#     print("x = ", x1)
# elif y_diff == 0:
#     print("Уравнение прямой, проходящей через эти точки:")
#     print("y = ", y1)
# else:
#     k = y_diff / x_diff
#     b = y2 - k * x2

# print("Уравнение прямой, проходящей через эти точки:")
# print("y = ", k, " * x + ", b)
# 3 ==========================================================================
# def summa(N):
#     summa = 0
#     summ = 0
#     summa = N * (N + 1) / 2  # Это второй способ, первый с помощью цикла for
#     print('Сумма чисел от 1 до', N, ':', summa)
#     while N > 0:
#         last_num = N % 10
#         summ += last_num
#         N //= 10
#     print('Сумма чисел: ', summ, end='\n\n')
#     return summ
#
# def number_of_digits(N):
#     num = N
#     quantity = 0
#     while N > 0:
#         N //= 10
#         quantity += 1
#     print('Кол-во цифр в числе', num, ':', quantity)
#     return quantity
#
# N = int(input('Введите число: '))
#
# difference = summa(N) - number_of_digits(N)
#
# print('\nРазность суммы и кол-ва цифр: ', difference)
# 4 ==========================================================================
# def Rev(Num):
#     Rev_num = ''
#     while Num > 0:
#         Rev_num += str(Num % 10)
#         Num //= 10
#     return Rev_num
#
# def reverse(N):
#     integer_part_of_number = int(N)     # Целая часть числа
#     print('Целая часть: ', integer_part_of_number)
#     Rev_int = int(Rev(integer_part_of_number))
#     print('Целая часть числа в обратном порядке: ', Rev_int)
#
#     fractional_part_of_number = round(N - int(N), 10)     # Дробная часть числа
#     print('Дробная часть: ', fractional_part_of_number)
#
#     dev_coef = 1
#     while fractional_part_of_number % 1 != 0:
#         fractional_part_of_number = round(fractional_part_of_number * 10, 7)
#         dev_coef *= 10
#     fractional_part_of_number = int(fractional_part_of_number)
#     print(fractional_part_of_number)
#     Rev_fract = float(Rev(fractional_part_of_number))/dev_coef
#     print('Дробная часть числа в обратном порядке: ', Rev_fract)
#
#     result = Rev_int + Rev_fract
#
#     return result
#
# N = float(input('Введите первое число: '))
# K = float(input('Введите второе число: '))
# print('='*80)
# print('Первое число наоборот: ', reverse(N))
# print('='*80)
# print('Второе число наоборот: ', reverse(K))
# 5 ==========================================================================
# def min_dev(N):
#     for devider in range(2, N + 1):
#         if N % devider == 0:
#             min_devider = devider
#             break
#     return min_devider
#
# N = int(input('Введите натуральное число: '))
# print('Наименьший делитель, отличный от единицы: ', min_dev(N))
# 6 ==========================================================================
# import math
#
# def check(x, y, R):
#     if math.sqrt(x ** 2 + y ** 2) < R:
#         result = 'Монетка где-то рядом'
#     else:
#         result = 'Монетки в области нет'
#     return result
#
# print('Введите координаты монетки:')
# x = float(input('X: '))
# y = float(input('Y: '))
# R = float(input('Введите радиус: '))
#
# print(check(x, y, R))
# 7 ==========================================================================
first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')

for year in range(first_year, second_year + 1):
    for i in range(10):
        year_1 = year
        count = 0
        while year_1 > 0:
            num = year_1 % 10
            if num == i:
                count += 1
            year_1 //= 10
        if count == 3:
            print(year)
# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
