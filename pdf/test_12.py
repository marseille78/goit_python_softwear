from datetime import datetime

current_day = '2024-12-07'
requested_day = datetime.strptime(current_day, "%Y-%m-%d").date()
print("requested_day: ", requested_day)

today_date = datetime.now().date()
print("today_date: ", today_date)

diff_day = today_date - requested_day
print(f"Days: {diff_day.days}")
print(f"Weeks: {diff_day.days // 7}")