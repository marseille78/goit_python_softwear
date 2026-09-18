# Привітання з Днем народження

from datetime import datetime, timedelta

def build_greeting_calendar(birthdays: dict, month: str) -> dict:
    greeting_calendar = dict()
    current_year = datetime.now().year

    for birth_day_str, names in birthdays.items():
        birth_date = datetime.strptime(birth_day_str, "%d-%m-%Y")
        # 17-13-1999 -> 17-03-2026
        current_birthday = datetime(current_year, birth_date.month, birth_date.day)
        # 17-03-2024 -> March

        if current_birthday.strftime("%B") != month:
            continue

        print("current_birthday.weekday(): ", current_birthday.weekday())
        if current_birthday.weekday() >= 5: # Saturday or Sunday
            current_birthday += timedelta(days=(7 - current_birthday.weekday()))

        greeting_date_str = current_birthday.strftime("%Y-%m-%d")

        if greeting_date_str not in greeting_calendar:
            greeting_calendar[greeting_date_str] = []

        greeting_calendar[greeting_date_str].extend(names)

    return greeting_calendar

birthday = {
    "14-02-1988": ["Slava", "Anna"],
    "15-03-1967": ["Olga"],
    "17-13-1999": ["Anton", "Alex"],
}

print(build_greeting_calendar(birthday, "March"))