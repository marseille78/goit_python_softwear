# Errors

try:
    value_x = input("Enter value x: ")
    value_y = input("Enter value y: ")

    value_final = -float(value_x) / float(value_y)
except Exception as e:
    print(e)
else:
    print(f"Result final equal {round(value_final, 2)}")
finally:
    print("End of calculation")