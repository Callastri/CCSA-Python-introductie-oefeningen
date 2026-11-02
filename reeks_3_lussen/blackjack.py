waarde = 0

while waarde < 21:
  kaart = int(input())
  if kaart == 0:
    print(f"Voorzichtig gespeeld ({waarde})")
    break
  waarde += kaart
  # print(f"kaart: {kaart}")
if waarde == 21:
  print(f"Gewonnen!")
elif waarde > 21:
    print(f"Verbrand ({waarde})")
