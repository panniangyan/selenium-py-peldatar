#Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be!
# A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!
#A megoldást egy fordito.py nevű file-ban kell beadnod.

num = -1
paros = []

while num != 0:
    num = int(input("Adj meg egy pozitív egész számot: "))
    if num < 0:
        continue
    elif num == 0:
        break
    elif num % 2 == 0:
        paros.append(num)


paros.reverse()
print(paros)






