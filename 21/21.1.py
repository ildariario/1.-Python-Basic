# Task 1

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

# Task 2



# Task 3



# Home Work
# 1 ==========================================================================

# 2 ==========================================================================

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