import random

# print(random.seed(version=2))
# print(random.getstate())
# print(random.randint(0, 100))
# print(random.randrange(0, 100, 7))
# print(random.choice(['black', 'white', 'red']))
print(random.choices(['black', 'white', 'red'], k=6, weights=[0, 7, 4]))