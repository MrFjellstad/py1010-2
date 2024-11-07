""""
Program for å samenligne den årlige kostnaden ved å eie en elbil eller en bensinbil.
 Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
 Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
 Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
 Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
 Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
"""
Forsikring_elbil = 5000             # 5000 kr/år
Forsikring_bensinbil = 7500         # 7500 kr/år
Trafikkforsikringsavgift = 8.38     # 8.38 kr/dag
Strømpris = 2.00                    # 2.00 kr/kWh
Drivstoffbruk_elbil = 0.2           # 0.2 kWh/km
Drivstoffpris_elbil = Strømpris * Drivstoffbruk_elbil # 0.4 kr/km
Drivstoffpris_bensinbil = 1.0       # 1.0 kr/km
Bomavgift_elbil = 0.1               # 0.1 kr/km
Bomavgift_bensinbil = 0.3           # 0.3 kr/km

Dager_pr_år = 365                   # Antall dager i året
Kjørte_km = 10000                   # Antatt kjørelengde per år

# Årlig kostnad for elbil
Årlig_forbruk_elbil = Drivstoffpris_elbil * Kjørte_km
Årlig_forsikring_elbil = Forsikring_elbil + (Trafikkforsikringsavgift * Dager_pr_år)
Årlig_bomavgift_elbil = Bomavgift_elbil * Kjørte_km

Årlig_kostnad_elbil = Årlig_forbruk_elbil + Årlig_forsikring_elbil + Årlig_bomavgift_elbil

# Årlig kostnad for bensinbil
Årlig_forbruk_bensinbil = Drivstoffpris_bensinbil * Kjørte_km
Årlig_forsikring_bensinbil = Forsikring_bensinbil + (Trafikkforsikringsavgift * Dager_pr_år)
Årlig_bomavgift_bensinbil = Bomavgift_bensinbil * Kjørte_km

Årlig_kostnad_bensinbil = Årlig_forbruk_bensinbil + Årlig_forsikring_bensinbil + Årlig_bomavgift_bensinbil

# Sammenligning av kostnader
if Årlig_kostnad_elbil < Årlig_kostnad_bensinbil:
    print(f"Elbil er billigst med en årlig kostnad på {Årlig_kostnad_elbil:.2f} kr mot {Årlig_kostnad_bensinbil:.2f} kr for bensinbil")
else:
    print(f"Bensinbil er billigst med en årlig kostnad på {Årlig_kostnad_bensinbil:.2f} kr mot {Årlig_kostnad_elbil:.2f} kr for elbil")


