# Task 1

# if ((1.1 + 2.2) == 3.3):
#     print('Равна')
# else:
#     print('Не равна')

# Task 2

# print(1.1 + 2.2)

# Task 3



# Home Work
# 1 ==========================================================================
# def calculation(tax, new_tax):      # tax - общая сумма налога, new_tax - новый налог
#     if tax + new_tax == tax:
#         print('Хуёво, бюджет не изменился.')
#     else:
#         print('Заебись, бюджет увеличился.')

# tax = float(input('Введите бюджет страны: '))
# new_tax = float(input('Новые поступления (налог): '))

# calculation(tax, new_tax)
# 2 ==========================================================================
def eqv(a, b, d):
    eps = 1e-15     # степень точности: до 15-го знака после точки
    c = a + b
    flag = abs(c - d) < eps
    print(flag)

first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))
thirdh_num = float(input('Введите третье число: '))

eqv(first_num, second_num, thirdh_num)
# 3 ==========================================================================

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