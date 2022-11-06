from __future__ import unicode_literals
from typing import List, Optional
import youtube_dl

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


keyword = "pure water"


def main():
    links = get_links(keyword)
    download_videos(links)


def get_links(query: str) -> List[str]:
    """
    Given a query, download all Youtube video results on the first page.

    :param query: term to search on Youtube
    :return: list of links to videos on first results page
    """
    keywords = query.split(" ")
    url_params: Optional[str] = None
    if len(keywords) > 1:
        url_params = "+".join(keywords)
    else:
        url_params = query
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/results?search_query=" + url_params)

    # find url by xpath and put into links list
    user_data: List[WebElement] = driver.find_elements("xpath", '//*[@id="video-title"]')
    links: List[str] = []
    for web_element in user_data:
        links.append(web_element.get_attribute('href'))
    # print links list
    print(links)
    # get rid of the first None object in the list
    links.pop(0)
    return links


# method to download videos from list
def download_videos(video_links_list: List[str], download_options: dict = {}) -> None:
    """
    Given a list of youtube links, download the videos.

    :param video_links_list: list of links to youtube videos
    :param download_options: dict containing download options regarding video/sound quality
    :return: None
    """
    # TODO give user option to specify folder to download to
    for video_link in video_links_list:
        with youtube_dl.YoutubeDL(download_options) as ydl:
            ydl.download([f'{video_link}'])


if __name__ == "main":
    main()
