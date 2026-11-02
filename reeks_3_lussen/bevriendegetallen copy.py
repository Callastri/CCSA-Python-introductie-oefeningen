def som_delers(getal):
  som = 0
  for i in range(1, getal):
    if getal % i == 0:
      som += i
  return som

a = int(input())
b = int(input())

if (som_delers(a) == b and som_delers(b) == a):
  print(f"{a} en {b} zijn bevriende getallen")
else:
  print(f"{a} en {b} zijn geen bevriende getallen")
