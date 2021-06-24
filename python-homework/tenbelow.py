#Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz. Írja ki ezek után a beolvasott számok összegét!

osszeg = 0
szam = int(input("Adj meg egy számot: "))


while szam < 10:
    osszeg += szam
    if osszeg >= 10:
        break
    szam = int(input("Adj meg egy számot: "))

print (f"Beolvasott számok összege: {osszeg}")

