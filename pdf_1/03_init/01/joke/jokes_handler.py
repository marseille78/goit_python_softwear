import random
from pathlib import Path

# print("__file__: ", Path(__file__))

current_dir = Path(__file__).parent

# print("current_dir: ", current_dir)

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
