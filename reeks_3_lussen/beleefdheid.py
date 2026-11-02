n = int(input())
aantal = 0

for start in range(1, n):   # for kiest het startgetal
  som = 0                   # opnieuw beginnen bij elk startgetal
  getal = start
  while som < n:            # while telt de opeenvolgende getallen op vanaf startgetal
    som += getal
    getal += 1
  if som == n:
    aantal += 1

print(aantal)