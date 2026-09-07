# Nonlocal

def outer_func():
    counter = 0

    def inner_func():
        nonlocal counter
        counter += 1
        print(counter)

    inner_func()
    inner_func()

outer_func()