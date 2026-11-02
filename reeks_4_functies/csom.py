def csom(getal):
  som = 0
  
  while getal > 0:
      som += getal % 10 
      getal = getal // 10
      
      if getal == 0 and som > 9:
          getal = som
          som = 0  # niet vergeten om de som terug op 0 te zetten, anders maak ik een oneindige loop.

  return som
  
print(csom(8))
print(csom(5436))
print(csom(377096267))

    
