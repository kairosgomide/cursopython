#5.44 Tipos Númericos

from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(7))
print(1.1 + 2.2)

getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))

print(1.1 + 2.2)
print(Decimal(1.1) + Decimal(2.2))