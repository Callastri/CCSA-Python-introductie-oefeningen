import math

a = float(input())
b = float(input())
c = float(input())

# delta berekenen
delta = b ** 2 - 4 * a * c     # Δ = b² - 4ac

# berekeningen binnen de if zetten - als ik deze er voor zet krijg ik foutmeldingen
if delta < 0:
    print("geen wortels")
elif delta == 0:
    print("een wortel")
    wortel = -b / (2 * a)
    print(wortel)
else:
    print("twee wortels")
    wortel1 = (-b + math.sqrt(delta)) / (2 * a)
    wortel2 = (-b - math.sqrt(delta)) / (2 * a)
    print(min(wortel1, wortel2))
    print(max(wortel1, wortel2))