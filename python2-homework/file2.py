# Olvasd be a fájlt,
# tárold a sorokat listában,
# majd írd ki a lista tartalmát egy sorban

text_list = []
with open('adat.txt', 'r') as adat:
    line = adat.read().replace("\n", " ")
    text_list.append(line)

print(text_list)

