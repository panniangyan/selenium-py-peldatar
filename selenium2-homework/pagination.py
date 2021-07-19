# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/pagination.html oldalt.
# Mentsd le az összes kontaktot az oldalról akinek a keresztneve (First Name) A betüvel kezdődik.
# A kiválasztott kontaktok összes adatát mentsd le memóriába egy szotár (dict) struktúrába.
# Amikor megvagy az összes adatot mentsd ki egy CSV file-ba.

import time
import pprint
import csv
from selenium import webdriver


PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/pagination.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
extracted_data = []
header = ["id", "first_name", "second_name", "surname", "second_surname", "birth_date"]

try:
    browser.get("http://localhost:9999/pagination.html")
    while True:
        time.sleep(2)
        table = browser.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text[0] == 'A':
                data_row["id"] = cells[0].text
                data_row["first_name"] = cells[1].text
                data_row["second_name"] = cells[2].text
                data_row["surname"] = cells[3].text
                data_row["second_surname"] = cells[4].text
                data_row["birth_date"] = cells[5].text
                extracted_data.append(data_row)
        next_button = browser.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

    pprint.pp(extracted_data)
    print(len(extracted_data))

    with open('pagination_out.csv', 'w') as out:
        writer = csv.DictWriter(out, fieldnames=header)
        for data in extracted_data:
            writer.writerow(data)

finally:
    browser.close()





