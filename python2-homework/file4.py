#Olvasd be a fájlt,
# tárold a sorokat listában,
# majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba

text_list = []
with open('adat.txt', 'r') as adat:
    line = adat.read()
    text_list.append(line)

with open('file4_out.txt', 'w') as out:
    for i in text_list:
        out.write(i)