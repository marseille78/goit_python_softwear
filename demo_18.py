# Функции

# Function of adding two numbers
def add(value_one: int, value_two: int) -> int:
    """
    Function of adding two numbers

    Input:
    :param value_one: integer
    :param value_two: integer

    Output:
    :return: integer
    """
    return value_one + value_two

sum_value: int = add(6, 9)

print(sum_value)