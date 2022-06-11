'''Работа за преподавателем'''
# Task 1

# def calculate_tax(price, tax):      # price - цена; tax - налог
#     total = price + (price * tax / 100)
#     print(total)

# myPrice = float(input('Введите цену: '))
# myTax = int(input('Введите налог (в %): '))

# calculate_tax(myPrice, myTax)

# Task 2

# def calculate_tax(price, tax):      # price - цена; tax - налог
#     tax += 10
#     total = price + (price * tax / 100)
#     print(total)
#     return total

# myPrice = float(input('Введите цену: '))
# myTax = int(input('Введите налог (в %): '))

# totalPrice = calculate_tax(myPrice, myTax)
# print(myTax)

# newTax = int(input('Введите новый налог (в %): '))

# totalPrice = calculate_tax(totalPrice, newTax)
# print('Итоговая цена: ', totalPrice)

# Task 3

# def numeral_count(number):     # number - число
#     if number < 0:
#         print('Число отрицательное! Обнуляю.')
#         return 0

#     count = 0
#     while number > 0:
#         number //= 10
#         count += 1
#     return count

# firstTask = int(input('Введите первое число: '))    # первая задача
# secondTask = int(input('Введите второе число: '))   # вторая задача

# firstNumeral = numeral_count(firstTask)     # numeral - цифра; number - число
# secondNumeral = numeral_count(secondTask)

# if firstNumeral > secondNumeral:
#     print('Цифр больше в первом числе.')
# elif firstNumeral < secondNumeral:
#     print('Цифр больше во втором числе.')
# else:
#     print('Равное кол-во цифр!')

# Home Work
# 1 ==========================================================================
'''Задача 1. Сумма чисел 2
Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое 
положительное число N и находит сумму всех чисел от 1 до N включительно. Функция 
вызывается два раза: сначала от числа N, а затем от полученной суммы.

Пример работы программы:
Введите число: 5
Сумма от 1 до 5 = 15
Сумма от 1 до 15 = 120
'''
# def summa_n(number):
#     summ = 0
#     for num in range(1, number + 1):
#         summ += num
#     print('Сумма от 1 до', number, '=', summ)
#     return summ

# N = int(input('Введите число: '))
# new_N = summa_n(N)
# N = summa_n(new_N)
# 2 ==========================================================================
'''Задача 2. «Назад в будущее»
Вы — один из разработчиков языка программирования Python, и вы пишете специальный 
математический модуль, который можно было бы просто подключить внутри программы и 
облегчить жизнь всем программистам.
Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает 
наибольший общий делитель этих двух чисел.

Пример работы программы:
Введите первое число: 6
Введите второе число: 10
НОД = 2
'''
# def gcd(num_1, num_2):
#     while num_1 != 0 and num_2 != 0:
#         if num_1 > num_2:
#             num_1 %= num_2
#         else:
#             num_2 %= num_1
#     GCD = num_1 + num_2
#     print('НОД = ', GCD)
#     return GCD

# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))

# result = gcd(num_1, num_2)
# 3 ==========================================================================
'''Задача 3. Приоритет задач
В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, 
а затем уже идут небольшие. Каждая из этих задач, по сути, просто огромный поток цифр. 
Ваша задача, как программиста этого центра, написать программу, которая поможет определять, 
какую из задач нужно решать в первую очередь. 
Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше 
всего цифр, и вывести на экран соответствующее сообщение. Если число отрицательное, то 
считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.

Пример работы программы:
Введите кол-во задач: 4
Введите число: 6
Введите число: 14
Введите число: 1
Введите число: 13434

Первая задача на обработку: 13434
'''
def numeral_count(number):
    if number < 0:
        print('Число отрецательное! Обнуляю.')
        return 0

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
    
N = int(input('Введите кол-во задач: '))
max_count = 0
for num in range(N):
    number = int(input('Введите число: '))
    current_count = numeral_count(number)
    if current_count > max_count:
        max_count = current_count
        max_num = number

print('Первая задача на обработку: ', max_num)
