# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/another_form.html oldalt.
# A program segítségével olvassd be a csv tartalmat.
# A feladatod, hogy az oldalon található formanyomtatvány segítségével
# feltöltsd a táblázatot. Használd a Python CSV könyvtárát.
# A feltöltött táblázatot ellenőrizheted
# ha a programod letölti a táblázat alatti gomb segítségével az aktuális tartalmat.
# Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.


from selenium import webdriver
import csv
import time


PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/another_form.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

def find_and_clear_by_id(id):
    element = browser.find_element_by_id(id)
    element.clear()
    return element


submit_button = browser.find_element_by_id("submit")


with open('table_in.csv', 'r') as table_in:
    reader = csv.reader(table_in, skipinitialspace=True, delimiter=',')
    next(reader)

    for row in reader:
        print(row)
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1])
        year, month, day = row[2].split('-')
        dob = [month, day, year]
        find_and_clear_by_id("dob").send_keys(dob)
        find_and_clear_by_id("phone").send_keys(row[3])
        submit_button.click()

        time.sleep(2)


browser.quit()
