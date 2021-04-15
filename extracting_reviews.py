"""
Final Project Title: IMDB Recommendation System

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
from webdriver_manager.chrome import ChromeDriverManager


def fetch_movie_reviews(review_title: str) -> dict:
    """
    Return a dictionary, where the key is the title of the review and the value
    is the description corresponding to the title. Takes in a set of titles and returns
    the reviews for those
    """

    # First we need to set up the browser
    # options = Options()
    # options.add_argument("--headless")
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Go to google the Browser
    browser.get('https://www.google.com')

    # Enters movie name + imbd in the google search bar:
    browser.find_element_by_name('q').send_keys(review_title + " imdb")
    time.sleep(1)

    # Click the google search button
    browser.find_element_by_name("btnK").send_keys(Keys.ENTER)
    time.sleep(1)

    # Click the link
    browser.find_element_by_xpath("""/ html / body / div[7] / div / div[9] / div[1] / div / div[2] / div[2] / div / div / div[
        1] / div / div / div / div / div[1] / a / h3""").click()
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
    """..."""

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.google.com')

    browser.find_element_by_name('q').send_keys(review_title + " trailer")
    time.sleep(1)

    browser.find_element_by_name("btnK").send_keys(Keys.ENTER)
    time.sleep(1)

    browser.find_element_by_xpath(
        "/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/h3/a/h3"
        ).click()
    time.sleep(5)
    browser.find_element_by_xpath("//body").send_keys("f")


