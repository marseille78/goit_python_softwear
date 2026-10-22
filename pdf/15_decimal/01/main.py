# print(0.1 + 0.2 == 0.3) # False
# print(0.1 + 0.2) # 0.30000000000000004

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))