# Task 1

# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# for i_elem in range(2, 8):
#     print(nums[i_elem], end=' ')
#
# print()
#
# for i_elem in range(2, 8):
#     print(new_nums[i_elem], end=' ')

# Task 2

def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [3, 4, 3]
answer = []

for i_nums in range(0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print('Исходный список: ', nums)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)

# Task 3



# Task 4 (Этого нет в уроке, это мои эксперименты)

# list_3 = [1, 2, 3, 4, 5]
# list_4 = []
# for i in range(5):
#     list_4.append(list_3[i])
# list_3[2] = 10
# print(list_3)
# print(list_4)
#
# print()
#
# list_5 = [1, 2, 3, 4, 5]
# list_6 = list_5[:]
# list_5[2] = 10
# print(list_5)
# print(list_6)

# Home Work
# 1 ==========================================================================
# import random
#
# original_prices = [random.randint(-10, 10) for _ in range(5)]
# new_prices = original_prices[:]
# for i in range(len(new_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
# ----------------------------------------------------------------------------
# import random
#
# original_prices = [random.randint(-10, 10) for _ in range(5)]
# new_prices = [(0 if i_elem < 0 else i_elem) for i_elem in original_prices]
#
# print(original_prices)
# print(new_prices)
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
# 2 ==========================================================================
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print('Исходный список: ', nums)
#
# print('1.', nums[:5])         # Выводит первые пять элементов списка.
# print('2.', nums[:8])         # Выводит весь список, кроме последних двух элементов.
# print('3.', nums[::2])        # Выводит все элементы с чётными индексами.
# print('4.', nums[1::2])       # Выводит все элементы с нечётными индексами.
# print('5.', nums[::-1])       # Выводит все элементы в обратном порядке.
# print('6.', nums[-1::-2])     # Выводит все элементы списка через один в обратном порядке,
#                               # начиная с последнего.
# #----------------------------------------------------------------------------------
# print('7.', nums[-2:-6:-1])   # Выводит все элементы списка в обратном порядке ,
#                               # начиная с -2-го с конца списка и до -6-го не всключая его.
# print('8.', nums[-2:6:-1])    # Выводит все элементы списка в обратном порядке, начиная с -2-го
#                               # с конца списка и до 6-го с начала списка не всключая его с конца.
# print('9.', nums[1::])        # Выводит весь список, начиная с элемента с индексом 1.
#                               # Stop - по умолчанию равен длине списка т.е. 10.
# print('10.', nums[-8::-1])    # Выводит весь список, начиная с элемента с индексом -8 и до конца.
#                               # Stop - по умолчанию равен длине списка взятым с отрицательным знаком
#                               # т.к. двигаемся с конца списка т.е. -10.
# 3 ==========================================================================
# import random
#
# A = random.randint(0, 2)
# B = random.randint(3, 6)
# print('A =', A, '\nB =', B)
#
# N = int(input('Сколько чисел в списке? '))
# list_1 = [random.randint(0, 101) for _ in range(N)]
# print('Исходный список: ', list_1)
# list_1[A:B + 1] = []
# print('Обработанный список: ', list_1)
# 4 ==========================================================================
# list_1 = [51, 92, 3, 35, 46, 72, 78, 92, 91, 77]
# print('Исходный список: ', list_1)
# list_1[1:6] = []
# list_1[-1] = []
# print('Обработанный список: ', list_1)
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