# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról.
# A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük,
# hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad.
# A {} jelek ne legyenek benne a fájlnévben.

#https://www.analyticsvidhya.com/blog/2020/08/web-scraping-selenium-with-python/


from selenium import webdriver
import time
import urllib.request


driver = webdriver.Chrome()
count = 0

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(5):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:
            cat_id = j.find_element_by_tag_name("p").text[8:]
            image_url = driver.find_element_by_tag_name("img").get_attribute("src")
            save_name = f"/home/student/PycharmProjects/selenium-py-peldatar/selenium2-homework/cats/{count+1}_{cat_id}.jpg"
            count = count + 1
#            urllib.request.urlretrieve(image_url, save_name)
            print(save_name, image_url, j.find_element_by_tag_name("p").text)
            if count == 20:
                quit()
        load_more.click()


finally:
    time.sleep(10)
    driver.quit()

