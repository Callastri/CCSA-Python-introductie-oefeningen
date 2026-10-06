km_aanvang = float(input())
km_afgifte = float(input())
aantal_liter = float(input())
aantal_km = km_afgifte - km_aanvang
verbruik = aantal_liter / (km_afgifte - km_aanvang) * 100
print(verbruik)