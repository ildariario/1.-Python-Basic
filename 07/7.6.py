# Home Work
# 1 ==========================================================================

# for num in 114, 12, 14, 10605, 4907, 450:
#     if num % 2 == 0 and num % 3 != 0:
#         print('Число:', num, '- подходит!')
#     else:
#         print('Число:', num, '- неподходит!')

# 2 ==========================================================================
# positive = 0
# for num in range(1, 11):
#     # print(num)
#     print(num, '-й номер:')
#     N = int(input('Введите число: '))
#     if N > 0 and N % 2 == 0:
#         positive += 1
# print('Одновременно четными и положительными являются', positive, 'номеров.')

# 3 ==========================================================================
# year_salary = 0
# for month in range(1, 13):
#     salary = int(input(f'Введите зарплату за {month}-й месяц: '))      # salary - зарплата
#     year_salary += salary
# aver = year_salary / month
# print(f'Средняя зарплата за {month} месяцев: ', aver)

# 4 ==========================================================================
# quantity = int(input('Сколько пингвинов показать? '))   # quantity - количество
# for num in range(quantity):
#     print('   _~_    ')
#     print('  (o o)   ')
#     print(' /  V  \  ')
#     print('/(  _  )\ ')
#     print('  ^^ ^^   ')

# 5 ==========================================================================
# violation = 0
# for sectors in range(30, 36):
#     people = int(input('Людей в ' + str(sectors) + ' секторе: '))
#     if people < 10:
#         print('Всё спокойно.')
#     else:
#         print('Нарушение! Слишком много людей в секторе!')
#         violation += 1                                      # violation - нарушение
# print('Количество нарушений: ', violation)

# 6 ==========================================================================
# x_0 = int(input('Введите начало отрезка: '))
# x_N = int(input('Введите конец отрезка: '))
# for X in range(x_0, x_N+1):
#     Y = X**3 + 2*X**2 - 4*X + 1
#     print('Функция Y(X='+ str(X) + ') равна:', Y)

# 7 ==========================================================================
# n = int(input('Введите натуральное число (любое >1 и не дробное): '))
# for num in range(100, 1000):
#     if num // 100 + num // 10 % 10 + num % 10 == n:
#         print(num)

# 8 ==========================================================================
# factorial = 1
# n = int(input('Введите натуральное число (любое >1 и не дробное): '))
# for num in range(1, n+1):
#     factorial = factorial*num
# print('Факториал числа', n,'равен', factorial)

# 9 ==========================================================================
# N = int(input('Сколько человек в классе? '))
# count_3 = 0
# count_4 = 0
# count_5 = 0
# for num in range(1, N+1):
#     grade = int(input('Какую оценку получил '+ str(num)+'-й человек? '))
#     if grade == 3:
#         count_3 += 1
#     elif grade == 4:
#         count_4 += 1
#     else:
#         count_5 += 1
# if count_3 > count_4 and count_3 > count_5:
#     print('Сегодня больше троечников!')
# elif count_4 > count_3 and count_4 > count_5:
#     print('Сегодня больше ударников!')
# else:
#     print('Сегодня больше отличников!')  

# 10 ==========================================================================
# a = int(input('Введите левую границу отрезка: '))
# b = int(input('Введите правую границу отрезка: '))
# sum = 0
# count = 0
# for num in range(a, b+1):
#     if num % 3 == 0:
#         sum += num
#         count += 1
#         print(str(count)+'-е число кратное трем: '+str(num))
# print('Сумма чисел кратных трем: ', sum)
# print('Всего чисел кратных трем: ', count)
# print('Среднее арифметическое всех чисел из отрезка [a; b],\nкоторые кратны числу три, равно:',sum/count)

# 11 ==========================================================================
# N = int(input('Введите число бактерий:  '))
# a = int(input('Стартовая температура в первой пробирке: '))
# b = int(input('Конечная температура в первой пробирке: '))
# quantity_1, quantity_2 = N, N
# # quantity_1 = N
# # quantity_2 = N
# for temp in range(a, b+1):
#     quantity_1 *= temp
# print('Популяция в первой пробирке: ', quantity_1)
# c = int(input('Стартовая температура во второй пробирке: '))
# d = int(input('Конечная температура во второй пробирке: '))
# for temp in range(c, d+1):
#     quantity_2 *= temp
# print('Популяция в второй пробирке: ', quantity_2)
# print('Разность популяции: ', abs(quantity_2 - quantity_1))

# 12 ==========================================================================
# quant_num = 0
# for num in range(10, 100):
#     if 3 * (num % 10) * (num // 10) == num:
#         print(num)

# 13 ==========================================================================
# N = int(input('Введите количество ступенек: '))
# steps = ''
# for num in range(1, N+1):
#     steps = steps + str(num)
#     print(steps)

N = int(input('Введите количество ступенек: '))
steps = 0
for num in range(1, N+1):
    steps = steps + num
    print(steps)
    steps *= 10
# 14 ==========================================================================
# n_prev = int(input('Введите первое число: '))
# flag = True
# for num in range(2, 11):
#     n_next = int(input('Введите следующее число: '))
#     if n_next < n_prev:
#         flag = False
#     n_prev = n_next
# if flag:
#     print('Числа по возрастанию упорядочены!')
# else:
#     print('Числа по возрастанию не упорядочены!')

# 15 ==========================================================================
# N = int(input('Сколько карточек в игре? '))
# sum_1 = 0
# sum_2 = 0
# for num in range(1, N+1):
#     sum_1 += num
# # print('Сумма номеров всех карточек = ', sum_1)
# for num in range(1, N):
#     num = int(input('Введите номер '+ str(num) +'-й карточки: '))
#     sum_2 += num
# print('````````````````````````````````\nНомер потерянной карточки: ', sum_1 - sum_2,'\n````````````````````````````````')


