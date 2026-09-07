# Функции

def sum_of_all_numbers(main_number, *numbers): # *agrs -> (2, 3, 4, 5, 6, 7, 8, 9)
    print(main_number)
    print(numbers)
    sum = 0
    for value in numbers:
        try:
            sum += float(value)
        except TypeError:
            continue
        except ValueError:
            continue
    return sum

print(sum_of_all_numbers(2, 3, 4, '1000', 5, 6, 7, 8, 7.7, 9, 'true', False, -90, sum([1, 2, 3, 4, 99])))