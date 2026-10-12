from joke import get_random_joke


def main():
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}")

    while True:
        user_reponse = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()

        if user_reponse == "так":
            print(get_random_joke())
        elif user_reponse == "ні":
            print(f"До побачення, {name}!")
            break


if __name__ == "__main__":
    main()