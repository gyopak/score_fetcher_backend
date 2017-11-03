from settings import *
from bs4 import BeautifulSoup
import dryscrape
import json


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
    group_matches = []
    for i in range(min(len(home_teams), len(away_teams))):
        group_matches.append(get_match_data(home_teams[i], away_teams[i]))
    return group_matches

def get_match_data(home, away):
    data = {}
    data["home_name"] = home.find(TEAM_HTML_ATTRIBUTE, {"class": TEAM_NAME_CLASS}).text
    data["away_name"] = away.find(TEAM_HTML_ATTRIBUTE, {"class": TEAM_NAME_CLASS}).text
    data["home_score"] = home.find("td", {"class": lambda L: HOME_SCORE_CLASS in L }).text
    data["away_score"] = away.find("td", {"class": lambda L: AWAY_SCORE_CLASS in L}).text
    data["time"] = home.find("td", {"class": lambda L: "time" in L }).text
    data["id"] = home["id"].split("_")[-1]
    return data
