def waardering(prijs, koers):
    bigmac_usa = 4.07
    percentage = (((prijs / bigmac_usa) - koers) / koers * 100)
    
    if percentage <= -25.00:
        return "sterk ondergewaardeerd"
    elif percentage <= -5.00:
        return "ondergewaardeerd"
    elif percentage <= 5.00:
        return "ongeveer gelijk"
    elif percentage <= 25.00:
        return "overgewaardeerd"
    else:
        return "sterk overgewaardeerd"



def wisselkoersanalyse(tekst, koers):
    delen = tekst.split(" ", 1)
    prijs = float(delen[0])   # OPLETTEN, hier de gesplitte list gebruiken en niet oorspronkelijke tekst.
    munt = delen[1]          # OPLETTEN, hier de gesplitte list gebruiken en niet oorspronkelijke tekst.
    oordeel = waardering(prijs, koers)
    return f"De {munt} is {oordeel} ten opzichte van de dollar."



print(wisselkoersanalyse("3.44 euro", 0.70))
print(wisselkoersanalyse("2.39 pond sterling", 0.62))