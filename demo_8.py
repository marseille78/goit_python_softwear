# Последовательность Фибоначчи

num_one, num_two = 0, 1

for _ in range(10):
    print(num_one, end=' ')
    num_one, num_two = num_two, num_one + num_two