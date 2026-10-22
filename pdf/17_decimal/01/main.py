from decimal import Decimal, ROUND_DOWN


# Вихідне число Decimal
number = Decimal("3.14159")
# number = 3.14159


# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal("0.00"), rounding=ROUND_DOWN)


print(rounded_number)