# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/forms.html oldalt.
# Koncentrálj a dátum mezőkre.
# A célod, hogy a következő képen látható dátum és idő értékekete pontosan beállítsd az alkalmazásba selenium segítségével:
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)


browser.find_element_by_id("example-input-date").send_keys("06-05-2021")
browser.find_element_by_id("example-input-date-time").send_keys("2012-05-05-05-05-05-555")
browser.find_element_by_id("example-input-date-time-local").send_keys("05120020001201PM")

browser.find_element_by_id("example-input-month").send_keys("d", Keys.ARROW_RIGHT, "1995")
browser.find_element_by_id("example-input-week").send_keys("522015")
browser.find_element_by_id("example-input-time").send_keys("1225AM")

time.sleep(2)
browser.quit()

