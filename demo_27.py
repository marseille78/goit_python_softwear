# Фибоначчи

def fibonacci(number):
    return number if number == 0 or number == 1 else\
        fibonacci(number - 2) + fibonacci(number - 1)

print(fibonacci(10))

# pow(2, 3)
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print(pow(2, 3))
print(power(2, 3))