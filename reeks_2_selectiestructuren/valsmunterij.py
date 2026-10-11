res_weging = input()
muntstukken = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if res_weging == "links":
  res_weging = input()
  if res_weging == "evenwicht":
    muntstukken[3] == muntstukken[4]
    result = muntstukken[5]
  elif res_weging == "links":
    muntstukken[3] > muntstukken[4]
    result = muntstukken[4]
  else:
    result = muntstukken[3]

elif res_weging == "rechts":
  res_weging = input()
  if res_weging == "evenwicht":
    muntstukken[0] == muntstukken[1]
    result = muntstukken[2]
  elif res_weging == "links":
    muntstukken[0] > muntstukken[1]
    result = muntstukken[1]
  else:
    result = muntstukken[0]

else:
  res_weging = input()
  if res_weging == "evenwicht":
    muntstukken[6] == muntstukken[7]
    result = muntstukken[8]
  elif res_weging == "links":
    muntstukken[6] > muntstukken[7]
    result = muntstukken[7]
  else:
    result = muntstukken[6]  

print(f"muntstuk #{result} is vervalst")