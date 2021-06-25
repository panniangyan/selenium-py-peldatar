#Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.

import time
from selenium import webdriver

PATH = "C:\\Windows\chromedriver.exe"
URL = ("https://progmasters.hu/")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

time.sleep(2)
browser.quit()
