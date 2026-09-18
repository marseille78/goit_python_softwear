"""
Розглянемо таке завдання. Наприклад лікар прописала пацієнтові приймати ліки протягом 45 днів.
Треба знати дату закінчення приймання ліків від поточної дати.
"""

from datetime import datetime, timedelta

current_day = datetime.now()
print("current_day: ", current_day)

interval = timedelta(days=10)
end_of_healing_process = current_day + interval
days_before_healing = current_day - interval

print("end_of_healing_process: ", end_of_healing_process)
print("days_before_healing: ", days_before_healing)