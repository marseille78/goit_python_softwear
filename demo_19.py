# Функции

def multiply(number_one, number_two, number_three=None):
    if number_three is None:
        return number_one * number_two
    else:
        return number_one * number_two * number_three

print(multiply(2, 3))
print(multiply(2, 3, 5))