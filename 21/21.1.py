# Разбоор ДЗ
'''Задача 10. Своя функция zip (необязательная)
В самом конце собеседования вас неожиданно спросили: «Расскажите, что делает функция zip?». В итоге,
чтобы произвести максимальное впечатление, вы решили не только рассказать про неё, но и написать её аналог.
Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
Затем выведите на экран сам генератор и кортежи.

Пример:
Строка: abcd
Кортеж чисел: (10, 20, 30, 40)

Результат:
<generator object <genexpr> at 0x00000204A4234048>
('a', 10)
('b', 20)
('c', 30)
('d', 40)

Дополнительно: создайте полный аналог функции zip, то есть сделайте так, чтобы программа работала с любыми
итерируемыми типами данных.
'''
# # Этап 1 ======================================

# syms_str = 'abc'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = [(syms_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(len(syms_str))]
# print(pairs)

# # Этап 2 ======================================
#
# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = [(syms_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(shortest_seq_range(syms_str, nums_tpl))]
# print(pairs)

# Этап 3 ======================================

def shortest_seq_range(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abcd'
nums_tpl = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tpl[i_elem])
         for i_elem in range(shortest_seq_range(syms_str, nums_tpl)))
print(pairs)
for i_elem in pairs:
    print(i_elem)
