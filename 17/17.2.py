# Task 1

# squares = []
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)

# Task 2

# squares = [x ** 2 for x in range(10)]
# print(squares)

# Task 3

# def get_higher_price(percent, price):
#     return round(price * (1 + percent/100), 2)
#
#
# prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
# first_percent = int(input('Повышение на 1-й год: '))
# second_percent = int(input('Повышение на 2-й год: '))
#
# prices_first = [get_higher_price(first_percent, i_price)
#                 for i_price in prices_now]
# prices_second = [get_higher_price(second_percent, i_price)
#                  for i_price in prices_now]
#
# print('Сумма цен за каждый год: ', round(sum(prices_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2))

# Home Work
# 1 ==========================================================================
# A = int(input('Левая граница: '))
# B = int(input('Правая граница: '))
#
# first_list = [x ** 3 for x in range(A, B + 1)]
# second_list = [x ** 2 for x in range(A, B + 1)]
#
# print('Список кубов чисел в диапазоне от ', A, 'до', B, ':', first_list)
# print('Список квадратов чисел в диапазоне от ', A, 'до', B, ':', second_list)
# 2 ==========================================================================
# string = input('Введите строку: ')
# additional_sym = input('Введите дополнительный символ: ')
#
# first_list = [sym * 2 for sym in string]
# second_list = [sym + additional_sym for sym in first_list]
#
# print('Список удвоенных символов: ', first_list)
# print('Склейка с дополнительным символом: ', second_list)
# 3 ==========================================================================
def price_increase(percent, price):
    return round(price + price * percent / 100, 2)


price_list = []

for _ in range(5):
    i_price = float(input('Цена на товар: '))
    price_list.append(i_price)

X = int(input('Процент повышения цены на первый год: '))
Y = int(input('Процент повышения цены на второй год: '))

price_first_year = [price_increase(X, i_price) for i_price in price_list]
price_second_year = [price_increase(Y, i_price) for i_price in price_first_year]

print('Сумма цен за каждый год: ', round(sum(price_list), 2), round(sum(price_first_year), 2),
      round(sum(price_second_year), 2))
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
