numbers = [1, 4, 1, 3, 2, 5, 2, 6]


qs = {i ** 2 for i in numbers}
print("qs:", qs)


odd_squares = {x ** 2 for x in range(1, 10) if x % 2 != 0}
print("odd_squares:", odd_squares)