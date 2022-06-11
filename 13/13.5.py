'''Работа за преподавателем'''
# Task 1

import math

precision = float(input('Точность: '))    # precision - точность

result = 0
i = 0
addMember = 1

while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1

b = 60
print('-' * b)
print('| Результат: ', '\t\t|\t', result, '\t|')
print('-' * b)
print('| Констатнта Эйлера (e): ', '|\t', math.e, '\t|')
print('-' * b)
