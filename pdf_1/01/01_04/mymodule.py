# mymodule.py
def say_hello(name):
    return f"Hello, {name}!"


def main():
    print("You imported hello.py")
    print(say_hello("user"))


if __name__ == "__main__":
    main()