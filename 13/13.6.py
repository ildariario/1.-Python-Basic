# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
# def floating_point_format(num):
#     a = num
#     b = 0
#     if a >= 10:
#         while num >= 10:
#             num /= 10
#             b += 1
#         print('Формат плавающей точки: ', a * 10 ** -b, '* 10 **', b)
#     elif a < 1 and a > 0:
#         while num < 1:
#             num *= 10
#             b += 1
#         print('Формат плавающей точки: ', a * 10 ** b, '* 10 **', str(-b))
#     elif a >= 1 and a < 10:
#         print('Формат плавающей точки: ', a * 10 ** b, '* 10 **', str(-b))
#     else:
#         print('Число должно быть неотрицательным и большим нуля!')

# x = float(input('Введите число положительное число > 0: '))
# floating_point_format(x)
# 2 ==========================================================================
# def get_parent_names_total_length(father, mother):
#     count_f = 0
#     count_m = 0
#     for sym in father:
#         count_f += 1
#     print('Символов в ФИ отца: ', count_f)
#     for sym in mother:
#         count_m += 1
#     print('Символов в ФИ матери: ', count_m)
#     summ = count_f + count_m
#     return summ

# S_N_father = input('ФИ отца: ') # surname and name - фамилия и имя
# S_N_mother = input('ФИ матери: ') # surname and name - фамилия и имя

# S = get_parent_names_total_length(S_N_father, S_N_mother)
# print('Сумма символов: ', S)
# 3 ==========================================================================
# def search_max(a, b):
#     maxx = round((a + b + abs(a - b)) / 2, 2)
#     return maxx

# num_1 = float(input('Введите первое число: '))
# num_2 = float(input('Введите второе число: '))
# num_3 = float(input('Введите третье число: '))

# maxx = search_max(num_1, num_2)
# maxx = search_max(maxx, num_3)

# print('Наибольшее число: ', maxx)
# 4 ==========================================================================
# def reverse(num):
#     new_num = ''
#     while num > 0:
#         new_num += str(num % 10)
#         num //= 10

#     return int(new_num)

# N = int(input('Введите первое число: '))
# K = int(input('Введите второе число: '))
# print()

# rev_N = reverse(N)
# rev_K = reverse(K)

# print('Первое число наоборот: ', rev_N)
# print('Второе число наоборот: ', rev_K)
# print()

# sum_NK = rev_N + rev_K

# print('Сумма: ', sum_NK)
# print()

# rev_NK = reverse(sum_NK)

# print('Сумма наоборот: ', rev_NK)
# 5 ==========================================================================
# flag = True
# M = ''
# P = ''

# exp_num = input('Введите число в экспоненциальной форме записи: ')

# for sym in exp_num:
#     if sym != 'e' and flag == True:
#         M += sym
#     elif sym == 'e':
#         flag = False
#     else:
#         P += sym

# print('Мантисса введенного числа: ', M)
# print('Порядок введенного числа: ', P)
# 6 ==========================================================================
# import math

# precision = float(input('Точность: '))

# e = 0
# i = 0
# addMember = 1

# while addMember > precision:
#     addMember = 1/math.factorial(i)
#     e += addMember
#     i += 1

# print('Результат: ', e)
# print('Эталон: ', math.e)
# 7 ==========================================================================
# x = 0.001 * 1.496e11
# y = 0
# while True:
#     move = input('Марсоход на позиции ' + str(x) + ', ' + str(y) + ' введите команду: ')
#     if move == 'a':
#         x -= 1
#     elif move == 'd':
#         x += 1
#     elif move == 'w':
#         y += 1
#     else:
#         y -= 1
#     if move == 'stop':
#         print('Наихралася бля!, завершение программы ...')
#         break
# 8 Недоделка 2 ==========================================================================
# def check_num(num_1, num_2):
#     count_1 = 0
#     count_2 = 0
#     temp_1 = num_1
#     temp_2 = num_2

#     while temp_1 > 0:
#         count_1 += 1
#         temp_1 = temp_1 // 10   
#     while temp_2 > 0:
#         count_2 += 1
#         temp_2 = temp_2 // 10   
    
#     if count_1 < 3:
#         print("В первом числе меньше 3 цифр.")
#         return 0
#     if count_2 < 4:
#         print("Во втором числе меньше 4 цифр.")
#         return 0

#     if count_1 >= 3 and count_2 >= 4:
#         last_digit = num_1 % 10                                                       # Последняя цифра
#         first_digit = num_1 // 10 ** (count_1 - 1)                                    # Первая цифра
#         between_digits = num_1 % 10 ** (count_1 - 1) // 10                            # Промежуточные цифры
#         num_1 = last_digit * 10 ** (count_1 - 1) + between_digits * 10 + first_digit  # Изменённое число
#         print('Изменённое первое число:', num_1)

#         last_digit = num_2 % 10                                                       # Последняя цифра
#         first_digit = num_2 // 10 ** (count_2 - 1)                                    # Первая цифра
#         between_digits = num_2 % 10 ** (count_2 - 1) // 10                            # Промежуточные цифры
#         num_2 = last_digit * 10 ** (count_2 - 1) + between_digits * 10 + first_digit  # Изменённое число
#         print('Изменённое первое число:', num_2)

#         summ = num_1 + num_2

#         return summ

# first_n = int(input("Введите первое число, в котором должно быть не меньше трёх цифр: "))
# second_n = int(input("Введите второе число, в котором должно быть не меньше четырех цифр: "))
# print()

# summ = check_num(first_n, second_n)
# if summ != 0:
#     print('\nСумма чисел:', summ)
# else:
#     print('\nОшибка! Одно из двух чисел не соответствуют формату ввода...')
# 9.1 Степень числа ==========================================================================
# Это мой вариант решения, и он не совсем тот, как требовали решить
# def first_condition(a, n, c):
#     n -= 1
#     if n != 0:
#         a *= c
#         first_condition(a, n, c)
#     else:
#         print('Число A в степени B равно: ', a)

# def second_condition(a, n, c):
#     n -= 1
#     if n != 0:
#         a *= c
#         second_condition(a, n, c)
#     else:
#         print('Число A в степени B равно: ', 1/a)

# def power(a, n, c):
#     if n > 0:
#         first(a, n, c)
#     elif n == 0:
#         print('Число A в степени B равно: ', a)
#     else:
#         second(a, -n, c)

# a = float(input('Введите вещественное положительное число A: '))
# n = int(input('Введите целое число B: '))

# power(a, n, a)
# 9.2 Степень числа ==========================================================================
# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)
 
# print('A**B = ', power(float(input('Число A: ')), int(input('Число B: '))))
# ===========================================
# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * power(a, n - 1)

# a = float(input('Введите вещественное положительное число A: '))
# n = int(input('Введите целое число B: '))

# Pow = power(a, n)

# print('Число A в степени B равно: ', Pow)
# ===========================================
# def power_0(a, n):
#     if n == 0:
#         return 1

# def power_1(a, n):
#     return a * power_0(a, n - 1)

# def power_2(a, n):
#     return a * power_1(a, n - 1)

# def power_3(a, n):
#     return a * power_2(a, n - 1)

# a = 2
# n = 3
# Pow = power_3(a, n)

# print('Число A в степени n равно: ', Pow)
# print(f'Число {a} в степени {n} равно: ', Pow)
# ===========================================
# Ниже уже другая задача нахождения факториала также с помощью рекурсии, на ней тренировался и вникал
# def factorial(num):
#     if num == 1:
#         return 1
#     fact_n_minus_1 = factorial(num - 1)
#     return num * fact_n_minus_1

# num_fact = factorial(5)
# print(num_fact)

# ========================================
# def factorial_1(num):
#     if num == 1:
#         return 1

# def factorial_2(num):
#     return num * factorial_1(num - 1)

# def factorial_3(num):
#     return num * factorial_2(num - 1)

# num_fact = factorial_3(3)
# print(num_fact)
# 10 Маятник ==========================================================================
# def calculate(start_magnitude, stop_magnitude):
#     i = 0
#     while start_magnitude > stop_magnitude:
#         start_magnitude -= 0.084 * start_magnitude
#         i += 1
#     return i

# start_magnitude = int(input('Введите начальную амплитуду: '))
# stop_magnitude = float(input('Введите амплитуду остановки: '))
# print(calculate(start_magnitude, stop_magnitude))
# Решение с помощью рекурсии (есть ограничения на глубину рекурсии в 1000 итераций)=======================================
# def calculate(start_magnitude, stop_magnitude, i):
#     if start_magnitude < stop_magnitude:
#         return i
#     return calculate(start_magnitude - 0.084 * start_magnitude, stop_magnitude, i+1)

# i = 0
# start_magnitude = float(input('Введите начальную амплитуду: '))
# stop_magnitude = float(input('Введите амплитуду остановки: '))
# print(calculate(start_magnitude, stop_magnitude, i))
# 11 ==========================================================================
# Это мой способ решения, он оказался близок но не совсем верный
# print('='*60)
# h = 4
# count = 0

# # D = float(input('Введите максимально допустимый уровень опасности: '))
# max_level_of_danger = 0.01
# D = -1

# while abs(D - max_level_of_danger) >= 1e-5:
# # while abs(D) > max_level_of_danger:
#     count += 1
#     if D < 0: 
#         h = h - h / 2
#     else:
#         h = h + h / 2

#     D = h**3 - 3 * h**2 - 12 * h + 10

# print(f'new_D(h={h}) = {D} усл. ед.')
    
# print('Приблизительная глубина безопасной кладки: ', h)
# print('Кол-во итераций: ', count)
# ======================================================
# print('='*60)
# def calculation(current_D, max_danger, h, count):
#     eps = 1e-5
#     while abs(current_D - max_danger) >= eps:
#         count += 1
#         if current_D < 0: 
#             h = h - h / 2
#         else:
#             h = h + h / 2
#         current_D = h**3 - 3 * h**2 - 12 * h + 10
#     print('Кол-во итераций: ', count)
#     print(f'Уровень опасности на глубине {h} [метров] = {current_D} усл. ед.')
#     return h

# max_h = 4
# max_level_of_danger = float(input('Введите максимально допустимый уровень опасности: '))
# D = -1
# h = calculation(D, max_level_of_danger, max_h, 0)
# print('Приблизительная глубина безопасной кладки: ', h, 'метров.')
#=============================
# print('='*60)
# def calculation(current_D, max_danger, h):
#     count = 0
#     while abs(current_D) > max_danger:
#         count += 1

#         if current_D < 0: 
#             h = h - h / 2
#         else:
#             h = h + h / 2
#         current_D = h**3 - 3 * h**2 - 12 * h + 10
#     print(f'Уровень опасности на глубине {h} [метров] = {current_D} усл. ед.')
#     print('Кол-во итераций: ', count)
#     return h

# max_h = 4
# max_level_of_danger = float(input('Введите максимально допустимый уровень опасности: '))
# D = -1
# h = calculation(D, max_level_of_danger, max_h)
# print('Приблизительная глубина безопасной кладки: ', h, 'метров.')
# А это решение Skillbox - а ================================================
print('='*60)
def calculation(max_danger):
    d_to = 0        # Значение d от нуля
    d_from = 4      # Значение d до четырех
    count = 0
    h = (d_to + d_from) / 2
    D = h**3 - 3 * h**2 - 12 * h + 10
    print('Глубина:', h,'[метров]\t\t||\t Уровень опасности:', D, '[усл. ед.]')
    while abs(D) > max_danger:
        count += 1
        if D < 0: 
            d_from = h
        else:
            d_to = h
        h = (d_to + d_from) / 2
        D = h**3 - 3 * h**2 - 12 * h + 10
        print('Глубина:', h,'[метров]\t\t||\t Уровень опасности:', D, '[усл. ед.]')
    print('`'*100,'\nКол-во итераций: ', count)
    return h

max_danger = float(input('Введите максимально допустимый уровень опасности: '))
if max_danger < 0:
    print('Максимально допустимый уровень опасности должен быть > 0!')
else:
    h = calculation(max_danger)
    print('Приблизительная глубина безопасной кладки: ', h, 'метров.')
print('='*50)
# 12 ==========================================================================
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)

# precision = float(input('Введите точность: '))      # precision - точность
# x = float(input('Введите x: '))

# summ_of_series = 1                                  # summ_of_series - сумма ряда
# addMember = 1                                       # addMember - добавляемы член
# i = 2
# sign = 1                                            # sign - знак (числа)

# while abs(addMember) > precision:
#     sign *= -1
#     addMember = sign * power(x, i) / fact(i)
#     summ_of_series += addMember
#     i += 2

# print('Сумма ряда = ', summ_of_series)
# =====================================================
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fact(n - 1)

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n - 1)

# def summ_series(precision, x):
#     summ_of_series = 0
#     addMember = 1
#     n = 0

#     while abs(addMember) > precision:
#         addMember = power(-1, n) * power(x, 2 * n) / fact(2 * n)
#         summ_of_series += addMember
#         n += 1

#     return summ_of_series

# precision = float(input('Введите точность: '))
# x = float(input('Введите x: '))

# print('Сумма ряда = ', summ_series(precision, x))
# 13 ==========================================================================
# print('='*60)
# def annuity_payment(S, i, n):
#     K = (i * (1 + i)**n) / ((1 + i)**n - 1)
#     A = round(K * S, 2)
#     return A

# def calculate(S, i, n, count):
#     percent_payment = S * i                                # percent_payment - выплата процентов
#     loan_body = annuity_payment(S, i, n) - percent_payment  # loan body - тело кредита

#     print('\nПериод', count)
#     print('Остаток долга на начало периода: ', S)
#     print('Выплачено процентов: ', percent_payment)
#     print('Выплаченая сумма в погашение основного долга: ', loan_body, end = '\n')
#     return loan_body

# S = float(input('Введите сумму кредита: '))
# n = int(input('На сколько лет выдан? '))
# i = int(input('Сколько процентов годовых? '))

# for count in range(1, 4):
#     loan_body = calculate(S, i/100, n, count)
#     S -= loan_body 
#     n -= 1
# else:
#     print('\nОстаток долга: ', S, '\n==================== ')
#     n_2 = int(input('На сколько лет продляется договор? '))
#     n += n_2
#     i = int(input('Увеличение ставки до: '))

#     for count in range(1, n + 1):
#         loan_body = calculate(S, i/100, n, count)
#         S -= loan_body
#         n -= 1

# print('Остаток долга: ', S)
# 14 ==========================================================================

# 15 ==========================================================================