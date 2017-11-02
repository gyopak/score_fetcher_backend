from settings import BASE_URL, GAME_TYPE
from bs4 import BeautifulSoup
import urllib


def get_page_data(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def make_soup():
    return BeautifulSoup(get_page_data(BASE_URL + GAME_TYPE))
