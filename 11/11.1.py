# 14 ==========================================================================
# rows = int(input('Введите кол-во уровней пирамиды: '))
# new_num = 1

# for line in range(rows):
#     space_count = rows - line - 1
#     print(space_count * '   ', end = '')
#     for number in range(line + 1):
#         print(new_num, end = '    ')
#         new_num += 2
#     print()
# 15 ==========================================================================
depth = int(input('Введите глубину ямы: '))

for line in range(depth):
    for left_number in range(depth, (depth - 1) - line, -1):
        print(left_number, end = '')
    point_count = 2 * ((depth - 1) - line)
    print('.' * point_count, end = '')
    for right_number in range(depth - line, depth + 1):
        print(right_number, end = '')
    print()
# 16 ==========================================================================


