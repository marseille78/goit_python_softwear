# Функции

def fn(a, **b):
    sum = 0
    for k in b:
        sum += b[k]
    return sum

result = fn(10, k=1, m=2, n=3, j=4)