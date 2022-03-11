# Task 1

# data = dict()
# data['server'] = {
#     'host': '127.0.0.1',
#     'port': '10'
# }
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty'
#     }
# }
#
# print(data)
# print(data['server']['port'])
# data['configuration']['ssh']['login'] = 'Vova'
# print(data['configuration']['ssh']['login'])
# print()
# for i_value in data.values():
#     for j_key in i_value:
#         print(j_key, i_value[j_key])

# Task 2

# data = dict()
# # до этого что-то происходит
# print(data.get('server'))
#
# data['server'] = {
#     'host': '127.0.0.1',
#     'port': '10'
# }
# # до этого что-то происходит
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин!')
#
# print(data.get('configuration', {}).get('ssh', {}).get('login', {}))
#
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty',
#     }
# }
#
# print(data)

# Task 3

# players_dict = {
#     1: {'name': 'Vanya',
#         'team': 'A',
#         'status': 'Rest'
#         },
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_a_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
#
# print(team_a_members)

# Home Work
# 1 ==========================================================================
# family_member = dict()
# family_member['name'] = 'Jane'
# family_member['surname'] = 'Doe'
# family_member['hobbies'] = ['running', 'sky diving', 'singing']
# family_member['age'] = 35
# family_member['children'] = [{'name': 'Alice', 'age': 6}, {'name': 'Bob', 'age': 8}]
#
# if family_member.get('children')[1].get('name') != 'Bob':
#     print('Bob - Noname')
# elif family_member.get('children')[1].get('name') != 'Rob':
#     print('Rob - Noname')
# 2 ==========================================================================
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
rest_members = [i_value['name']
                for i_value in players_dict.values()
                if i_value['team'] == 'A' and i_value['status'] == 'Rest']
training_members = [i_value['name']
                for i_value in players_dict.values()
                if i_value['team'] == 'B' and i_value['status'] == 'Training']
travel_members = [i_value['name']
                for i_value in players_dict.values()
                if i_value['team'] == 'C' and i_value['status'] == 'Travel']
print('1.', rest_members)
print('2.', training_members)
print('3.', travel_members)
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
