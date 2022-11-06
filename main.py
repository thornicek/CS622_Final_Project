from __future__ import unicode_literals
from typing import List, Any
import youtube_dl


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keyword = "short+sample+video"
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=" + keyword)
# find url by xpath and put into links list
user_data = driver.find_elements("xpath", '//*[@id="video-title"]')
links: List[Any] = []
for i in user_data:
    links.append(i.get_attribute('href'))
# print links list
for x in range(len(links)):
    print(links[x])
# get rid of the first None object in the list
links.pop(0)

# method to download videos from list
def download_videos(list):
    ydl_opts = {}
    for i in links:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{i}'])


download_videos(links)
