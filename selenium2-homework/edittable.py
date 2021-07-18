# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt.
# A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
#       a) Adj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
#       b) Ellenőrizd a kereső funkciót.
#       c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/editable-table.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)


def add_data(my_input_data, my_row):
    for i in range(0, 4):
        cell = browser.find_element_by_xpath(f'/html/body/div/div/div[2]/table/tbody/tr[{my_row}]/td[{i + 1}]/input')
        cell.send_keys(my_input_data[i])


def change_data_value(my_data, my_cell):
    cell = browser.find_element_by_xpath(f'/html/body/div/div/div[2]/table/tbody/tr[{my_cell[0]}]/td[{my_cell[1]}]/input')
    print(cell.get_attribute("value"))
    cell.clear()
    cell.send_keys(my_data)
    print(cell.get_attribute("value"))
    assert (my_data == cell.get_attribute("value"))


def search(my_word):
    search_btn = browser.find_element_by_xpath("//*[@id='container']/div/div[1]/input")
    search_btn.send_keys(my_word)
    print(search_btn.text)
    cell = browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[1]/td[1]/input')
    if cell.get_attribute("value") == "":
        return "nincs találat"
    assert(cell.get_attribute("value") != "")
    time.sleep(2)
    search_btn.send_keys(Keys.BACK_SPACE * len(my_word))


add_btn = browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/button')

# sor hozzáadása, kitöltése
add_btn.click()
input_data = ["körte", "15", "2", "gyümölcs2"]
row = 7
add_data(input_data, row)

add_btn.click()
input_data = ["alma", "1", "1", "gyümölcs"]
row = 8
add_data(input_data, row)
time.sleep(2)

# ellenőrizd a kereső funkciót
word = "alma"
search(word)
time.sleep(2)

# változtass meg egy értéket és ellenőrizd
change_data_value("PANNI", [2, 2])

time.sleep(2)
browser.quit()









#name = browser.find_element_by_xpath('html/body/div/div/div[2]/table/tbody/tr[8]/td[1]/input')
#price = browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[8]/td[2]/input')
#quantity = browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[8]/td[3]/input')
#category = browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[8]/td[4]/input')

#name.send_keys("alma", Keys.ENTER)
#price.send_keys("25", Keys.ENTER)
#quantity.send_keys("3", Keys.ENTER)
#category.send_keys("gyümölcs", Keys.ENTER)

#cell = browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[1]/td[1]/input')
#old_value = cell.get_attribute("value")
#cell.clear()
#new_input = "Panni"
#cell.send_keys(new_input)
#new_value = cell.get_attribute("value")
#assert(new_input == new_value)




