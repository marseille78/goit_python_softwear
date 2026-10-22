from decimal import Decimal, getcontext


getcontext().prec = 6
print(Decimal("1") / Decimal("7"))


getcontext().prec = 8
print(Decimal("1") / Decimal("7"))