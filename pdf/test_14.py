from datetime import datetime, date

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def day_of_year(full_date): # 2021-02-13
    year, month, day = full_date.split("-")
    day_of_week = datetime(year=int(year), month=int(month), day=int(day)).weekday()
    return days_name.get(day_of_week)

print(day_of_year("2026-09-10"))