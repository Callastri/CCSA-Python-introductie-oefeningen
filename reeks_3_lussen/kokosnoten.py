# p = int(input())
# k = int(input())
# totaal = k

# a = k   #aantal kokosnoten dat de piraat in de hoop aantreft als hij 's nachts opstaat
# b = 0   #aantal kokosnoten dat de piraat 's nachts verstopt
# c = 0   #aantal kokosnoten dat de piraat 's nachts aan de aap geeft
# d = 1   #volgnummer van de piraat

# for piraat in range (p):
  
#   if a > 0:
#     b = a // p
#     c = a % p
#     k = a - b - c
#     if d <= p:
#       if c == 1:
#         print (f"{a} noten = {b} noten voor piraat#{d} en {c} noot voor de aap")
#       elif c > 0: 
#         print (f"{a} noten = {b} noten voor piraat#{d} en {c} noten voor de aap")
#       else:
#         print (f"{a} noten = {b} noten voor piraat#{d} en geen noten voor de aap")
#     d += 1
#     a = k       
#     if d == p + 1:  
#       b = a // p
#       c = a % p
#       if c == 1:
#         print (f"elke piraat krijgt {b} noten en {c} noot voor de aap")
#       elif c > 0: 
#         print (f"elke piraat krijgt {b} noten en {c} noten voor de aap")
#       else:
#         print (f"elke piraat krijgt {b} noten en geen noten voor de aap")


# verbeterde code hieronder
p = int(input())
k = int(input())

a = k     # aantal noten in de hoop

for d in range(1, p + 1):
  b = a // p    # aantal noten die piraat d verstopt
  c = a % p     # aantal noten voor de aap
  if c == 0:
    aap = "geen noten"
  elif c == 1:
    aap = "1 noot"
  else:
    aap = f"{c} noten"
  print (f"{a} noten = {b} noten voor piraat#{d} en {aap} voor de aap")
  a = a - b - c

#ochtend
b = a // p
c = a % p
if c == 0:
  aap = "geen noten"
elif c == 1:
  aap = "1 noot"
else:
  aap = f"{c} noten"
print (f"elke piraat krijgt {b} noten en {aap} voor de aap")