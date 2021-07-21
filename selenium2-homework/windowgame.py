# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/windowgame.html oldalt.
# A feladatot, hogy megtalád a random kiválasztott színhez tartozó gombot.
# Ha egy gombra rákattintasz az egy új ablakot fog feldobni, egy valamilyen színben tündököl.
# Ügyelj arra, hogy ne árassza el a képernődet a sok ablak.

from selenium import webdriver


PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/windowgame.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

color = browser.find_element_by_id('target_color')
print(color.text)
main_window = browser.window_handles[0]
buttons = []

for i in range(100):
    button = browser.find_element_by_xpath(f'//*[@id={i}]').click()
    other_window = browser.switch_to.window(f'{i}_win')
    button_color = browser.find_element_by_xpath('/html/body/h1')
    buttons.append(button_color.text)
    print(i+1, buttons[i])
    browser.close()
    browser.switch_to.window(main_window)
    if buttons[i] == color.text:
        print(color.text)
        print(browser.find_element_by_xpath('//*[@id="numberOfGuesses"]').text)
        break

browser.close()
browser.quit()


