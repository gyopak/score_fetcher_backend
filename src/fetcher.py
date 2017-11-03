from src.settings import BASE_URL, GAME_TYPE, TEAM_HTML_ATTRIBUTE, TEAM_CLASS, SOUP_FORMAT
from bs4 import BeautifulSoup
import dryscrape
import urllib


def get_page_data(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def make_soup():
    session = dryscrape.Session()
    session.visit(BASE_URL + GAME_TYPE)
    return BeautifulSoup(session.body(), SOUP_FORMAT)


def get_teams():
    return make_soup().find_all(TEAM_HTML_ATTRIBUTE, {"class": TEAM_CLASS})
