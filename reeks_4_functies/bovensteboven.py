def bovensteboven(getal):
    tekst = str(getal)
    omgekeerd = tekst[::-1]
    newtekst = ""
  
    for c in omgekeerd:    
        if c in "018":
            newtekst += c
        elif c == "6":
            newtekst += "9"
        elif c == "9":
            newtekst += "6"
        else:
            return False
       
    return newtekst == tekst

def volgende(n):
    getal = n + 1
    while not bovensteboven(getal):
        getal += 1
    return getal

print(bovensteboven(689))
print(bovensteboven(1961))
print(bovensteboven(2965))
print(bovensteboven(68089))
print(bovensteboven(90306))
  
print(volgende(689))
print(volgende(1961))
print(volgende(98765))