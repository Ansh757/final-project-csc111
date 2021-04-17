"""
Final Project Title: Top3

Objective: Fetch the reviews from the internet and converting it into a CSV file such that
we can use it for the UI

By: Ansh Malhotra, Armaan Mann, Leya Abubaker, Gabriel Pais

This file is Copyright (c) 2020 Ansh Malhotra, Armaan Mann, Leya Abubaker
"""
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from typing import Dict, List
from webdriver_manager.chrome import ChromeDriverManager


####################################################################################################
# Helper Functions implemented for the GUI.
####################################################################################################
def getdata(url: str) -> str:
    """Returns the HTML text for the specified url that is entered."""
    r = requests.get(url)
    return r.text


def fetch_movie_reviews(review_title: str) -> dict:
    """Return a dictionary, where the key is the title of the review and the value
    is the description corresponding to the title. Takes in a set of titles and returns
    the reviews for those.
    """

    # First we need to set up the browser
    headless = Options()
    headless.add_argument("--headless")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=headless)

    # Go to google the Browser
    browser.get('https://www.google.com')

    # Enters movie name + imbd in the google search bar:
    browser.find_element_by_name('q').send_keys(review_title + " imdb")
    time.sleep(1)

    # Click the google search button
    browser.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]
    """).send_keys(Keys.ENTER)
    time.sleep(1)

    # Click the link
    browser.find_element_by_xpath("""/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]
    /div/div/div/div[1]/div/div/div[1]/a/h3""").click()
    time.sleep(5)

    # Click the user reviews
    browser.find_element_by_xpath(
        "//*[@id='quicklinksMainSection']/a[3]").click()

    # Fetch the IMBD reviews
    contain_url = browser.current_url
    link_request = requests.get(contain_url)
    extract_html = BeautifulSoup(link_request.content, "html.parser")
    search = extract_html.find(id="main")

    # Get the title of the movie
    element1 = search.find(class_="parent")
    element2 = element1.find(itemprop="name")
    element3 = element2.find(itemprop='url')

    # Review Title Extraction
    extract_review_title = search.select(".title")
    review_title = [raw_title.get_text().replace("\n", "") for raw_title in extract_review_title]

    # Review Description Title
    extarct_review_description = search.select(".content .text")
    review_description = \
        [raw_review_description.get_text() for raw_review_description in extarct_review_description]

    return {"Review Title": review_title,
            "Review Description": review_description}


def trailers(review_title: str):
    """Take a movie as the parameter and auto guides the user to the corresponding
    trailer on youtube"""

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.youtube.com')

    search_bar = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div['
                                               '3]/div[2]/ '
                                               'ytd-searchbox/form/div/div[1]/input')
    time.sleep(1)

    search_bar.send_keys(review_title + " trailer")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(1)

    browser.find_element_by_xpath(
        "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-"
        "renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/"
        "ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"
    ).click()
    time.sleep(5)
    browser.find_element_by_xpath("//body").send_keys("f")


def get_images(movie: str) -> str:
    """
    Returns the image address in the form on .jpg or .png where it webscrapes off the
    movieposterbd.com for the a movie of choice
    """
    movie_url = movie.replace(" ", "+")
    data_html = getdata("https://www.movieposterdb.com/search?category=title&q=" + movie_url)
    all_html_parsing = BeautifulSoup(data_html, 'html.parser')
    image_html_info = all_html_parsing.find_all('img')
    lst = image_html_info[2]['src']
    return lst


def filtering(movies: List[str]) -> Dict[str, str]:
    """Returns a dictionary, where the key is the title of the movie and the value is the
    link for the movie poster. Additionally, if the movie as an invalid link, the movie is skipped
    and next movie is considered.
    """
    lst = {}
    count = 0
    for m in movies:
        pick = get_images(m)
        if pick != 'https://posters.movieposterdb.com/no-posters-yet':
            lst[m] = pick
            count += 1
        if count == 3:
            break

    if len(lst) > 3:
        return lst
    else:
        try:
            len(lst) < 3
        except LookupError:
            print("Sorry, Chrome was not able to extract the pictures "
                  "for the given movie titles")


    # if len(lst) < 3:
    #     raise FileNotFoundError
    # else:
    #     return lst

# if __name__ == '__main__':
#     import python_ta.contracts
#     python_ta.contracts.check_all_contracts()
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 1000,
#         'disable': ['E1136', 'R0914', 'W0612'],
#         'extra-imports': ['csv', 'networkx', 'pandas',
#                           'time', 'requests', 'BeautifulSoup', 'bs4', 'selenium',
#                           'Options', 'Keys', 'ChromeDriverManager',
#                           'selenium.webdriver.common.keys', 'selenium.webdriver.chrome.options',
#                           'webdriver_manager.chrome'],
#         'allowed-io': ['movie_info'],
#         'max-nested-blocks': 4
#     })
