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