# Разбор ДЗ
'''Задача 15. (*необязательная)
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее,
зная номера оставшихся карточек.
Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
Программа должна вывести номер потерянной карточки.
'''
# Вар 1
# total_cards = int(input('Введите кол-во карточек: '))
# total_sum = 0
# remaining_sum = 0           # remaining - остальной, остальные
# for card in range(1, total_cards + 1):
#     total_sum += card
# for card in range(total_cards - 1):
#     remaining_card = int(input('Номер оставшейся карты: '))
#     total_sum -= remaining_card
# print('Номер потерявшейся карты: ', total_sum)

# Вар 2
# total_cards = int(input('Введите кол-во карточек: '))
# total_sum = 0
# remaining_sum = 0           # remaining - остальной, остальные
# total_sum = (1 + total_cards) / 2 * total_cards
# for card in range(total_cards - 1):
#     remaining_card = int(input('Номер оставшейся карты: '))
#     total_sum -= remaining_card
# print('Номер потерявшейся карты: ', int(total_sum))
