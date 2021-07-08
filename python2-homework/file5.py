# Olvasd be a fájlt,
# és írd ki a tartalmát egy másik fájlba,
# úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz

with open('adat.txt', 'r') as adat:
    with open('file5_out.txt', 'w') as out:
        out.write(adat.read())
