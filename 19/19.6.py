# Task 1


# Task 2


# Task 3


# Home Work
# 1 ==========================================================================

# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# for i_name in goods:
#     quantity = 0
#     price = 0
#     for i_list in store:
#         if goods[i_name] == i_list:
#             # print(i_name, '-', store[i_list])
#             for i_quantity in store[i_list]:
#                 quantity += i_quantity['quantity']
#                 price += i_quantity['price'] * i_quantity['quantity']
#             print('{} - {} шт, стоимость {} руб'.format(i_name, quantity, price))
# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================
# Сам не смог сделать!
# Вариант 1 --------------------------------------------
# N = int(input('Введите количество человек: '))
# tree = {}
# lvl_persons_in_tree = {}
#
# # Наполнение словарей tree и lvl_persons_in_tree
# for i_pair in range(N - 1):
#     child, parent = input(f'{i_pair+1} пара: ').split()
#     tree[child] = parent
#     lvl_persons_in_tree[child] = 0
#     lvl_persons_in_tree[parent] = 0
#
# # Вычисление уровней людей в дереве и заполнение ими значений словаря lvl_persons_in_tree
# for i_key in tree:
#     current_child = i_key
#     while current_child in tree:
#         current_child = tree[current_child]
#         lvl_persons_in_tree[i_key] += 1
#
# print('tree:', tree)
# for i_person in sorted(lvl_persons_in_tree):
#     print(i_person, lvl_persons_in_tree[i_person])
# Вариант 2 --------------------------------------------
def height(man):
    if man not in tree:
        return 0
    else:
        return 1 + height(tree[man])


tree = {}
N = int(input('Введите количество человек: '))
# Наполнение словаря tree
for i_pair in range(N - 1):
    child, parent = input(f'{i_pair+1} пара: ').split()
    tree[child] = parent
# Наполнение словаря tree
heights = {}
for man in set(tree.keys()).union(set(tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)
# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
