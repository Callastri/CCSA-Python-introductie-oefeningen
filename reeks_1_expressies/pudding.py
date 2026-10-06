aantal_stuks = int(input())
prijs_per_stuk = float(input())
aantal_barcodes = int(input())
aantal_mijl = int(input())

totaal_bedrag = float(aantal_stuks * prijs_per_stuk)
totaal_ontvangen_fm = aantal_stuks // aantal_barcodes *  aantal_mijl

print("Phillips spendeerde $" 
      + str(totaal_bedrag) + " voor " 
      + str(totaal_ontvangen_fm) + " frequent flyer mijlen.") 