from settings import BASE_URL, GAME_TYPE, SOUP_FORMAT
from bs4 import BeautifulSoup
import dryscrape


def make_soup():
    session = dryscrape.Session()
    session.visit(BASE_URL + GAME_TYPE)
    return BeautifulSoup(session.body(), SOUP_FORMAT)

def match_making(raw):
    pass    