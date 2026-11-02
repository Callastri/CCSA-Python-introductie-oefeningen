
import math

n = 100
fn = 0
kleinste_n = 0

for i in range (1, n + 1):
  fn += 1 / i ** 2 
  verschil = abs(fn - math.pi ** 2 / 6)
  if verschil <= 1 / 100 and kleinste_n == 0:
    kleinste_n = i

print (fn)
print (kleinste_n)

