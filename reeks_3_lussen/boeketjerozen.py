rw = int(input())
bw = int(input())
vergelijk = input()

for blauw in range(2, bw):
  wit  = bw - blauw
  rood  = rw - wit
  # print(f"blauw={blauw}  wit={wit}  rood={rood}  blauw+rood={blauw + rood}   blauw+wit={blauw + wit}")
  if wit >= 2 and rood >=2:
    br = blauw + rood
    if (vergelijk == "<" and br < bw) or (vergelijk == ">" and br > bw):
      print(blauw)
      print(wit)
      print(rood)