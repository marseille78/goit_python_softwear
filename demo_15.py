# Errors

try:
    value_x = input("Enter value x: ")
    value_y = input("Enter value y: ")

    value_final = -value_x / value_y
except TypeError:
    print("Type Error exception block")

    try:
        value_final = -float(value_x) / float(value_y)
    except ZeroDivisionError:
        print("Could not divide by zero")
    except ValueError:
        print("Error!!! Could not convert to float")
    else:
        print(f"Result final equal {round(value_final, 2)}")
else:
    print(f"Result final equal {round(value_final, 2)}")
finally:
    print("End of calculation")