from settings import BASE_URL, GAME_TYPE, SOUP_FORMAT, GAME_URL, GROUP_HTML_ATTRIBUTE, TEAM_HTML_ATTRIBUTE, GROUP_COUNTY_CLASS, GROUP_TOURNAMENT_CLASS
from bs4 import BeautifulSoup
import dryscrape


def make_soup():
    session = dryscrape.Session()
    session.visit(BASE_URL + GAME_URL)
    return BeautifulSoup(session.body(), SOUP_FORMAT)


def get_matches():
    raw = make_soup()
    groups= raw.find_all(GROUP_HTML_ATTRIBUTE, {"class": GAME_TYPE})
    matches = []
    for group in groups:
        matches.extend(get_match_by_group(group))
    return matches

def get_match_by_group(group):
    country = group.find(TEAM_HTML_ATTRIBUTE, {"class": GROUP_COUNTY_CLASS})
    tournament = group.find(TEAM_HTML_ATTRIBUTE, {"class": GROUP_TOURNAMENT_CLASS})
    match_parts = group.findAll("tr", {"id" : lambda L: L})
    home_teams = match_parts[::2]
    away_teams = match_parts[1::2]
    for home_team in home_teams:
            
