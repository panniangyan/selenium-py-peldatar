# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
# Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/usr/bin/chromedriver"
URL = "http://localhost:9999/videos.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)


def start_video(my_video):
    my_video.click()
    my_video.send_keys(Keys.SPACE)
    time.sleep(2)
    my_video.screenshot(f"{my_video.text}_screenshot.png")
    time.sleep(2)


#html5
html5_video = browser.find_element_by_id("html5video")
start_video(html5_video)

video1 = browser.find_element_by_id("video1")
browser.find_element_by_xpath("/html/body/div/button[1]").click()
time.sleep(2)
video1.screenshot(f"{video1.text}_screenshot.png")
time.sleep(2)

yt_video = browser.find_element_by_id("youtubeframe")
start_video(yt_video)

browser.quit()

