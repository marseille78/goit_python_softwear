# Рекурсия

def foo(number):
    print(number)
    if number < 10:
        foo(number + 1)

foo(0)