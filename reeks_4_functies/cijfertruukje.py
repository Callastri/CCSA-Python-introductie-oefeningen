def even_oneven(getal):
    getallen = str(getal)
    even = 0
    oneven = 0
    
    for g in getallen:
        if int(g) % 2 == 0:
            even += 1
        else:
            oneven += 1
    return (even, oneven)

print(even_oneven(886328712442992))
print(even_oneven(10515))
print(even_oneven(145))

def volgende(getal):
    even, oneven = even_oneven(getal)
    som = even + oneven
    nieuwgetal = int(str(even) + str(oneven) + str(som))
    return nieuwgetal

print(volgende(886328712442992))
print(volgende(10515))
print(volgende(145))

def stappen(getal):
    counter = 0
    while getal != 123:
        getal = volgende(getal)
        counter += 1
    return counter

print(stappen(886328712442992))
print(stappen(1217637626188463187643618416764317864))
print(stappen(0))
print(stappen(1))