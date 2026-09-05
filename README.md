# Python Software Engineering

## Зрізи у Python (Slice)

```py
s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]

odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]

even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)

```