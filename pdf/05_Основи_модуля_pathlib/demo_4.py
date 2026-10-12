from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")

print("original_path :> ", original_path)
print("new_path :> ", new_path)
