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


def assert_alerts(my_btn, my_text):
    my_btn.click()
    assert (browser.switch_to.alert.text == my_text)
    print(browser.switch_to.alert.text)


buttons = []
for i in range(1, 4):
    print(i)
    button = browser.find_element_by_xpath(f"/html/body/div/div[2]/input[{i}]")
    buttons.append(button)


ref_text = "I am alert"
assert_alerts(buttons[0], ref_text)
time.sleep(2)
browser.switch_to.alert.accept()

ref_text = "I am confirm"
assert_alerts(buttons[1], ref_text)
time.sleep(2)
browser.switch_to.alert.accept()

ref_text = "I am prompt"
assert_alerts(buttons[2], ref_text)
browser.switch_to.alert.send_keys("Panni")
time.sleep(2)
browser.switch_to.alert.accept()

paragraph = browser.find_element_by_xpath("//*[@id='demo']")
print(paragraph.text)
assert(paragraph.text != "")
time.sleep(2)

double_click_box = browser.find_element_by_id("double-click")
actions_chains = ActionChains(browser)
actions_chains.double_click(double_click_box).perform()
ref_text = "You double clicked me!!!, You got to be kidding me"
alert = browser.switch_to.alert
print(alert.text)
assert(alert.text == ref_text)
time.sleep(2)
alert.accept()

time.sleep(2)
browser.quit()
