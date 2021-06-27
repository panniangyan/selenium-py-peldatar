#Készíts egy Python alkalmazást ami selenium-ot használ.
# Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt.
# A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás.
# Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet.
# Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát.
# A megoldáshoz használj python try except struktúrát.


import time
from selenium import webdriver

PATH = "C:\\Windows\chromedriver.exe"
URL = ("https://progmasters.hu/")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

try:
    search = browser.find_element_by_id("nemletezik")
    print(search)
except:
    print("ID does not exist")


time.sleep(2)
browser.quit()