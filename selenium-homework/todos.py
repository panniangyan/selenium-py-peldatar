#Készíts egy Python alkalmazást ami selenium-ot használ.
#Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
#A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
#A feladatod, hogy kigyűjtsd az összes jelenleg aktív Todo bejegyzést.
#Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg.
#(Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).


from selenium import webdriver

PATH = "C:\\Windows\chromedriver.exe"
URL = ("http://localhost:9999/todo.html")

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

active_todo = browser.find_elements_by_xpath('//span[@class="done-false"]')

print ("jelenleg aktív Todo bejegyzések:")
for todo in active_todo:
    print ("- ",todo.text)



