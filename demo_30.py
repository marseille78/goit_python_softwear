"""
Програма "Вгадай число"
"""

from random import randint


def predict_number(number):
    goal = randint(0, number)
    counter = 0

    while True:
        user_input = int(input(f"Guess the number from 0 to {number}: "))
        counter += 1

        if user_input > goal:
            print("Smaller")
        elif user_input < goal:
            print("Larger")
        else:
            print(f"You win! Number of attempts: {counter}")
            break

predict_number(10)