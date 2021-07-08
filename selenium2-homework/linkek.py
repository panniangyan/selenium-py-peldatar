# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999 oldalt.
# Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket.
# A list tartalmát írd ki egy fájlba.
# Minden link egy új sorba kerüljön.
# A kimenetre írd ki hány linket találtál


from selenium import webdriver

PATH = "/usr/bin/chromedriver"
URL = ("http://localhost:9999")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

link_list = []

try:
    elements = browser.find_elements_by_xpath('//a[contains(@href,"")]')

    for i in elements:
        link_list.append(i.get_attribute("href"))

    with open('link.txt', 'w') as link:
        j = 0
        while j < len(link_list):
            link.writelines(link_list[j])
            link.writelines("\n")
            j = j + 1

    print(len(link_list), "linket találtam az oldalon")

except:
    print("Something went wrong")

finally:
    browser.quit()
