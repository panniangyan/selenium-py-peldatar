#Az autód 7 litert fogyaszt országúton és 9-et városban.
# A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
# Mennyit fogyaszt az autód csak oda?
# És oda-vissza?
# Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel
# (országúti fogyasztás, városi fogyasztás,
# országúton megtett út, városban megtett út, benzin ára)
# dolgozol, hanem a felhasználótól kéred ezeket be.
# Ahol szükséges, ne feledd konvertálni az értékeket!



orszaguti_fogyasztas = int(input("Hány liter benzit fogyaszt az autó országúton? "))
varosi_fogyasztas  = int(input("Hány liter benzit fogyaszt az autó a városban? "))
orszaguton_megtett_ut = int(input("Hány kilómétert tett meg az autó országúton? "))
varosban_megtett_ut = int(input("Hány kilómétert tett meg az autó városban? "))
benzin_ara = int(input("Mennyi a benzin literenkénti ára? "))

egy_ut_fogyasztas = orszaguti_fogyasztas * (orszaguton_megtett_ut/100) + varosi_fogyasztas * (varosban_megtett_ut/100)

oda_vissza_fogyasztas = egy_ut_fogyasztas * 2

oda_vissza_benzinkoltseg = oda_vissza_fogyasztas * benzin_ara

print(f"Egy út fogyasztás: {egy_ut_fogyasztas} L.")
print(f"Oda-vissza fogyasztás: {oda_vissza_fogyasztas} L.")
print(f"Oda-vissza út benzinköltsége: {oda_vissza_benzinkoltseg} Ft.")