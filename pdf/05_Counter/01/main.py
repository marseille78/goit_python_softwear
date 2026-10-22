from collections import Counter

# Створення Counter з рядка
letter_count = Counter("banana")

print(letter_count)
print("a: ", letter_count["a"])
print("n: ", letter_count["n"])