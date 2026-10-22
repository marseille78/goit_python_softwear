from collections import namedtuple

# Створення іменованого кортежу

Point = namedtuple('Point', ['x', 'y'])

print("Point: ", Point)

p = Point(11, y=22)

print('p.x: ', p.x)
print('p.y: ', p.y)