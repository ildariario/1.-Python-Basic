'''Работа за преподавателем'''
# Task 1

# # Вариант препода ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def print_tax_document(tax, *args):
#     tax_sum = 0
#     for i_price in args:
#         tax_sum += i_price * tax / 100
#     print('Суммарный налог для всех цен:', tax_sum)
#
#
# my_tax = int(input('Величина налога: '))
# print_tax_document(my_tax, 1000, 950, 880, 920, 990)
#
# # Мой вариант ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def print_tax_document(tax, *args):
#     tax_sum = sum(args) * tax / 100
#     print('Суммарный налог для всех цен:', tax_sum)
#
#
# my_tax = int(input('Величина налога: '))
# print_tax_document(my_tax, 1000, 950, 880, 920, 990)

# Task 2

# def print_tax_document(tax, *args, **kwargs):
#     tax_sum = sum(args) * tax / 100
#     print('Суммарный налог для всех цен:', tax_sum)
#     for i_info, i_value in kwargs.items():
#         print('{}: {}'.format(i_info, i_value))
#
#
# my_tax = int(input('Величина налога: '))
# print_tax_document(my_tax, 1000, 950, 880, 920, 990,
#                    year=1977, doc_type='Report', operation_id=1110034)
