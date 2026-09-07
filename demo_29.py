"""
Напишіть функцію format_string, яка центрує рядок у рамках заданої довжини length.

Задачі:

Створіть функцію format_string, яка приймає 2 аргументи: string рядок, який потрібно форматувати,
та length - довжина, у межах якої потрібно центрувати рядок. Якщо довжина string більша, або
дорівнює length, поверніть рядок без змін.
Якщо довжина string меньша за length, додайте перед рядком пробіли, для того, щоб рядок був
центрований у рамках length.
Кількість пробілів визначте за формулою (length - len(string)) // 2.
Поверніть з функції відформатований рядок, що центрується в межах length.

Очікуваний результат:

Функція format_string повертає відформатований рядок, відповідно до заданих правил.

Підказки:

Використовуйте len() для визначення довжини рядка. Для створення рядка з пробілів
використовуйте " " * кількість пробілів.
"""

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        total_spaces = length - len(string)
        space_left = total_spaces // 2
        space_right = total_spaces - space_left
        return "*" * space_left + string + "*" * space_right

print(format_string("now", 2))
print(format_string("now", 9))
print(format_string("now", 8))