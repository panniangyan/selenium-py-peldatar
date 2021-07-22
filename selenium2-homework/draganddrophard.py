# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/dragndrop2.html oldalt.
# A feladatod, hogy a todo oszlobpól átrakd az összes kártyát a doing oszlopba.


from selenium import webdriver
import time
from os import getcwd


def drag_drop_id_todo(my_source):
    source = browser.find_element_by_id(f'{my_source}')
    target = browser.find_element_by_id('Todo')
    browser.execute_script(JS_DRAG_DROP, source, target)


def drag_drop_id_done(my_source):
    source = browser.find_element_by_id(f'{my_source}')
    target = browser.find_element_by_id('Done')
    browser.execute_script(JS_DRAG_DROP, source, target)


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://localhost:9999/dragndrop2.html")

time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '/dnd.js', 'r').read()


list_elements = ['Pizza', 'Tacos', 'BBQ', 'Burgers']
for i in list_elements:
    drag_drop_id_todo(i)


list_elements.append('Macaroni')
for i in list_elements:
    print(i)
    drag_drop_id_done(i)

browser.implicitly_wait(5)

time.sleep(2)
browser.quit()
