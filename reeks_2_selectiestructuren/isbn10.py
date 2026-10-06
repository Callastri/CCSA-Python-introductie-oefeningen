som = 0
for i in range(9):
  cijfer = int(input())
  som += (i + 1) * cijfer

controle = int(input()
               )
if controle == som % 11:
  print('OK')
else:
  print('FOUT')