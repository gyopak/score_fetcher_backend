from settings import TEAM_HTML_ATTRIBUTE, TEAM_CLASS
from src.external.soup import make_soup


def get_raw():
    soup = make_soup()
    
    return soup.find_all(TEAM_HTML_ATTRIBUTE, {"class": TEAM_CLASS})
