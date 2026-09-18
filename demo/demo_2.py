# from datetime import *
import datetime

current_day = datetime.datetime.now()
date_today = datetime.datetime.today()

print(current_day, date_today, sep="\n")

print(f"Date: {current_day.date()}")
print(f"Time: {current_day.time()}")