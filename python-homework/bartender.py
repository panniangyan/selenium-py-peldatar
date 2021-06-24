#Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla. Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását. Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni. Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

kor = input("Hány éves vagy? ")
mit_iszol = input("Mit iszol? ")

italok = ("sör", "kóla")

if (int(kor) < 18 and mit_iszol == "sör"):
    print(f"Sajnos nem adhatok neked {mit_iszol}t.")
elif (int(kor) > 60 and mit_iszol == "kóla"):
    print("A koffein megemelheti a vérnyomását.")
elif (mit_iszol not in italok):
    print("Sajnos csak sört vagy kólát tudunk adni.")
else:
    print(f"Parancsoljon, a {mit_iszol}.")