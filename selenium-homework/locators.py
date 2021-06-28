#Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
# Gyakorlásképpen keress ki elemeket a képernyőről az alábbi kritériumoknak megfelelően:
#   ID alapján
#   NAME alapján
#   XPath kifejezéssel
# Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.

from selenium import webdriver

PATH = "C:\\Windows\chromedriver.exe"
URL = ("http://localhost:9999/kitchensink.html")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

match_by_id = browser.find_element_by_id("radio-btn-example")
print("ID text: ",match_by_id.text)
print("ID attribute: ",match_by_id.get_attribute("bmwradio"))

match_by_name = browser.find_element_by_name("courses")
print("NAME text: ",match_by_name.text)
print("NAME attribute: ",match_by_name.get_attribute("courses"))

match_by_xpath = browser.find_element_by_xpath('//button[@id="openwindow"]')
print("XPATH text: ",match_by_xpath.text)
print("XPATH attribute: ",match_by_xpath.get_attribute("openwindow"))

browser.quit()