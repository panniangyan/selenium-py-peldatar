#Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt.
# Használj id lokátort és keressd ki az elemenekt egyesével.
# A legelső olyan elemre ami button típusú kattints rá és ellenőrizd, hogy a helyes szöveg jelenik-e meg az elemek listája alatt.

import time
from selenium import webdriver

PATH = "C:\\Windows\chromedriver.exe"
URL = ("http://localhost:9999/trickyelements.html")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

i=1
while i <= 5:
    elem_id = browser.find_element_by_id(f'element{i}')
    if type(elem_id == "onclick"):
        elem_id.click()
        result = browser.find_element_by_id("result")
        if result.text == f"{elem_id.text} was clicked":
            print(result.text)
            break
        else:
            print (elem_id,": hibás szöveg.")
    else:
        print(elem_id," gomb nem létezik.")
    i = i + 1


#time.sleep(2)
#browser.quit()
