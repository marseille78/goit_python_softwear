"""
Розглянемо таке завдання. Наприклад лікар прописала пацієнтові приймати ліки протягом 45 днів.
Треба знати дату закінчення приймання ліків від поточної дати.
"""

from datetime import datetime

current_day = datetime.now()
print(current_day.timestamp())

day_zero = datetime.fromtimestamp(0)
print(day_zero)