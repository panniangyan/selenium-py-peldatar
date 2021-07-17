# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt.
# A tanultak alapján az összes alert funkcióra írj selenium kódot.
# A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy paragraf tagben, miután eltűnt az alert.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/alert_playground.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)



# alert button
alert_btn = browser.find_element_by_xpath("/html/body/div/div[2]/input[1]")
alert_btn.click()
ref_text = "I am alert"
alert = browser.switch_to.alert
assert (alert.text == ref_text)
print(alert.text)
time.sleep(2)
alert.accept()
time.sleep(2)

#confirmation box
confirmation_box_btn = browser.find_element_by_xpath("/html/body/div/div[2]/input[2]")
confirmation_box_btn.click()

ref_text = "I am confirm"
alert = browser.switch_to.alert
assert (alert.text == ref_text)
print(alert.text)
time.sleep(2)
alert.accept()
time.sleep(2)

prompt_box = browser.find_element_by_xpath("/html/body/div/div[2]/input[3]")
prompt_box.click()

ref_text = "I am prompt"
alert = browser.switch_to.alert
assert(alert.text == ref_text)
print(alert.text)
alert.send_keys("Panni")
time.sleep(2)
alert.accept()
time.sleep(2)

paragraph = browser.find_element_by_xpath("//*[@id='demo']")
print(paragraph.text)
assert(paragraph.text != "")

double_click_box = browser.find_element_by_id("double-click")
actions_chains = ActionChains(browser)
actions_chains.double_click(double_click_box).perform()
alert = browser.switch_to.alert
print(alert.text)
ref_text = "You double clicked me!!!, You got to be kidding me"
assert(alert.text == ref_text)
time.sleep(2)
alert.accept()
time.sleep(2)

