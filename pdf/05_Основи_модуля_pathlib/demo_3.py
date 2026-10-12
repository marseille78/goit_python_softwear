from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)
