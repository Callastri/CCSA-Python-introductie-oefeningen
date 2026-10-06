aantal_appels = int(input())
appels_per_kist = 20
appels_per_pallet = 35

tot_appel_kist = aantal_appels // 20
tot_appel_over = aantal_appels % 20
tot_pallet_gevuld = tot_appel_kist // 35
tot_kist_over = tot_appel_kist % 35

print(tot_pallet_gevuld)
print(tot_kist_over)
print(tot_appel_over)