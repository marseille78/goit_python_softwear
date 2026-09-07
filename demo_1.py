name = "Ruslan"
age = 48
has_driver_licence = True

print(bool(name))

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")