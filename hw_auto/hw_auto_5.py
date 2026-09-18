"""
1. Спочатку необхідно перевірити, чи дата народження birthday припадає на вихідний день.
У Python дні тижня нумеруються від 0 (понеділок) до 6 (неділя). Отже, субота та неділя матимуть індекси
5 та 6 відповідно. Умова перевірки дня тижня може бути записана як if birthday.weekday() >= 5:.

2. Якщо дата народження випадає на вихідний, необхідно знайти наступний понеділок.
Це робиться за допомогою функції find_next_weekday, до якої передається поточна дата народження
birthday і цільовий день тижня 0 (понеділок).

3. Якщо дата народження випадає на вихідний, функція adjust_for_weekend повинна повернути дату
наступного понеділка. Інакше, якщо дата народження випадає на будній день, повертається оригінальна
дата народження.
"""

"""
На п'ятому кроці ми виконаємо обробку вихідних днів.

Вам потрібно написати функцію adjust_for_weekend, яка приймає як аргумент дату народження
birthday і перевіряє, чи припадає ця дата на вихідний (суботу або неділю). Якщо дата народження
припадає на вихідний, функція знаходить наступний понеділок і повертає його як нову дату святкування.
Інакше, якщо дата народження випадає на будній день, функція повертає оригінальну дату народження.
"""

"""
Підказки:

1. Спочатку необхідно перевірити, чи дата народження birthday припадає на вихідний день.
У Python дні тижня нумеруються від 0 (понеділок) до 6 (неділя). Отже, субота та неділя матимуть індекси
5 та 6 відповідно. Умова перевірки дня тижня може бути записана як if birthday.weekday() >= 5:.

2. Якщо дата народження випадає на вихідний, необхідно знайти наступний понеділок.
Це робиться за допомогою функції find_next_weekday, до якої передається поточна дата народження
birthday і цільовий день тижня 0 (понеділок).

3. Якщо дата народження випадає на вихідний, функція adjust_for_weekend повинна повернути
дату наступного понеділка. Інакше, якщо дата народження випадає на будній день,
повертається оригінальна дата народження.
"""

# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday):


#     return birthday





from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return birthday.replace(day=find_next_weekday(birthday, 0).day)
    return birthday

start_date = string_to_date("2026.09.19")

print(":> ", adjust_for_weekend(start_date))