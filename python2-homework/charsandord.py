#Szavak előfordulási gyakorisága
#Állapítsuk meg, hogy az alábbi szövegben (TEXT) melyik szó hányszor fordul elő s írassuk ki az eredményt a következő formában: szó_1 előfordulások_száma_1 szó_2 előfordulások_száma_2 ...
#Az eredményt úgy írassuk ki, hogy a lista szavak szerint rendezve legyen. Minden szó kisbetűsen szerepeljen, vagyis pl. a 'The' és 'the' szavak azonos szónak számítanak.
#Használjuk az str.split() függvényt (paraméter nélkül) a whitespace karakterek eltávolítására.
#Az egyes szavakhoz kapcsolódó írásjelekkel (pont, vessző, idézőjel, stb.) nem kell most foglalkozni.


import string

text = open("text.txt", "r")

my_dict = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split()

    for word in words:
        if word in my_dict:
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1


for key in list(my_dict.keys()):
    print(key, " ", my_dict[key])