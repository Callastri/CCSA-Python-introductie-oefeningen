def maximale_blootstelling(waarde):
  tijdsduur = 0.0
  if waarde < 80:
    tijdsduur = -1.0
  else:
    max_seconden = 8.0 * 60.0 * 60.0
    blok = 0
    blok = (waarde - 80) // 3
    for i in range(int(blok)):
      max_seconden /= 2
    tijdsduur = max_seconden
  return tijdsduur

print(maximale_blootstelling(40))
print(maximale_blootstelling(60))
print(maximale_blootstelling(75))
print(maximale_blootstelling(80))
print(maximale_blootstelling(86))
print(maximale_blootstelling(90))
print(maximale_blootstelling(95))
print(maximale_blootstelling(97))
print(maximale_blootstelling(105))
print(maximale_blootstelling(107))
print(maximale_blootstelling(118))
print(maximale_blootstelling(115))
print(maximale_blootstelling(120))

