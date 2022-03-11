# Task 1

# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#     return sym_dict
#
#
# text = input('Введите текст: ').lower()
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ':', hist[i_sym])
#
# print('Максимальная частота: ', max(hist.values()))

# Task 2

# phonebook = {
#     'Ваня': 100,
#     'Петя': 200,
#     'Алиса': 300,
# }
#
# other_phonebook = {
#     'Игорь': 1000,
#     'Петя': 800,
#     'Алена': 2000,
# }
#
# phonebook.update(other_phonebook)
# print(phonebook)
# phonebook['Гоша'] = phonebook.pop('Игорь')
# print(phonebook)
# print(phonebook['Ваня'])
# print(phonebook.get('Степан'))

# Task 3


# Home Work

# 1 ==========================================================================
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
# print(big_storage)
#
# product_name = input('Введите название товара для поиска: ')
# if big_storage.get(product_name) == None:
#     print('Такого товара на складе "{}" нет!'.format('big_storage'))
# else:
#     print('Количество:', big_storage.get(product_name))
# 2 ==========================================================================
# def key_from_value(min_value):
#     for i_key in incomes:
#         if incomes[i_key] == min_value:
#             return i_key
#
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# total = sum(incomes.values())
# min_income = min(incomes.values())
# name_min = key_from_value(min_income)
# incomes.pop(name_min)
#
# print('Общий доход за год составил {} рублей'.format(total))
# print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(name_min, min_income))
# print('Итоговый словарь: ', incomes)
# 3 ==========================================================================
def histogram():
    for i_sym in text:
        if i_sym in sym_dict:
            sym_dict[i_sym] += 1
        else:
            sym_dict[i_sym] = 1
    return sym_dict


text = input('Введите текст: ')
sym_dict = dict()
hist = histogram()

for i_elem in sorted(hist.keys()):
    print(i_elem, ':', hist[i_elem])

print('Максимальная частота: ', max(hist.values()))
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
