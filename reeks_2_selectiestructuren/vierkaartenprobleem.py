
# vraag = input()
# if (vraag == "waarde"):
#   waarde = int(input())
# else:
#   kleur = input()
# draaien = input()

# if vraag == "waarde":
#   if waarde == 3 and draaien == "ja":
#     print(f"Fout: kaarten met waarde {waarde} moeten niet gedraaid worden.")
#   elif waarde == 3 and draaien == "nee":
#     print(f"Juist: kaarten met waarde {waarde} moeten niet gedraaid worden.")
#   elif waarde == 8 and draaien == "ja":
#     print(f"Juist: kaarten met waarde {waarde} moeten gedraaid worden.")
#   elif waarde == 8 and draaien == "nee":
#     print(f"Fout: kaarten met waarde {waarde} moeten gedraaid worden.")
# else:
#   if kleur == "rood" and draaien == "ja":
#     print(f"Fout: kaarten met kleur {kleur} moeten niet gedraaid worden.")
#   elif kleur == "rood" and draaien == "nee":
#     print(f"Juist: kaarten met kleur {kleur} moeten niet gedraaid worden.")
#   elif kleur == "bruin" and draaien == "ja":
#     print(f"Juist: kaarten met kleur {kleur} moeten gedraaid worden.")
#   elif kleur == "bruin" and draaien == "nee":
#     print(f"Fout: kaarten met kleur {kleur} moeten gedraaid worden.")

vraag = input()
if (vraag == "waarde"):
  waarde = int(input())
  moet_draaien = waarde % 2 == 0  
else:
  kleur = input()
  moet_draaien = kleur != "rood"
draaien = input()


if (draaien == "ja") == moet_draaien:
  resultaat = "Juist"
else:
  resultaat = "Fout"

if moet_draaien:
  regel = "moeten gedraaid worden"
else:
  regel = "moeten niet gedraaid worden"

kaart = waarde if vraag == "waarde" else kleur
print(f"{resultaat}: kaarten met {vraag} {kaart} {regel}.")