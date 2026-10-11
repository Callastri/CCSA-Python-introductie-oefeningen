begin_uur = int(input())
begin_minuut = int(input())
eind_uur = int(input())
eind_minuut = int(input())

begin = begin_uur * 60 + begin_minuut
eind = eind_uur * 60 + eind_minuut

achttienuur = 1080
eenentwintguurdertig = 1290
middernacht = 1440

geldig_begin = begin >= achttienuur and begin < middernacht
geldig_eind = eind <= middernacht and eind > achttienuur

cost1 = 2
cost2 = 4


if geldig_begin and geldig_eind:
  if begin < eenentwintguurdertig and eind <= eenentwintguurdertig:
    kost_vroeg = float((eind - begin)/60 * cost1)
    print(kost_vroeg)
  elif begin >= eenentwintguurdertig and eind > eenentwintguurdertig:
    kost_laat = float((eind - begin)/60 * cost2)
    print(kost_laat)
  else:
    kost_voor_2130 = float((eenentwintguurdertig - begin)/60 * cost1)
    kost_na_2130 = float((eind - eenentwintguurdertig)/60 * cost2)
    print(kost_voor_2130 + kost_na_2130)

else:
  print("ongeldige invoer")