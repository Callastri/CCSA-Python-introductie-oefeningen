a = int(input())
b = int(input())
som_a = 0
som_b = 0

for i in range(1, a):
  if (a % i == 0 and som_a <= b):
    som_a += i
    # print(som_a)

for i in range(1, b):
  if (b % i == 0 and som_b <= a):
    som_b += i
    # print(som_b)


if (som_a == b and som_b == a):
  print(f"{a} en {b} zijn bevriende getallen")
else:
  print(f"{a} en {b} zijn geen bevriende getallen")
