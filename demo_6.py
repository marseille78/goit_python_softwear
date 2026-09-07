# Тернарный оператор

value_x, value_y = 5, 7

# if value_x > value_y:
#     print(value_x)
# else:
#     print(value_y)

max_value = value_x if value_x > value_y else value_y

print(max_value)

value_a, value_b = 5, 5

max_value = 'A > B' if value_a > value_b else 'A < B' if value_a < value_b else 'A = B'

print(max_value)