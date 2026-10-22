from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)

print(d)