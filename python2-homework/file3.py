#Olvasd be a fájlt,
# tárold a sorokat listában,
# majd írd ki a lista tartalmát egy sorként egy másik fájlba

text_list = []
with open('adat.txt', 'r') as adat:
    line = adat.read().replace("\n", " ")
    text_list.append(line)

print(text_list)

with open('file3_out.txt', 'w') as out:
    for i in text_list:
        out.write(i)

