from settings import *
from bs4 import BeautifulSoup
from xvfbwrapper import Xvfb
import dryscrape
import json
import copy
import sys

#vdisplay = Xvfb()

def make_soup(url):
    #dryscrape.start_xvfb()
    session = dryscrape.Session()
    session.visit(url)
    return BeautifulSoup(session.body(), SOUP_FORMAT)
    


def get_matches():
    raw = make_soup(BASE_URL + GAME_URL)
    groups = raw.find_all(GROUP_HTML_ATTRIBUTE, {"class": GAME_TYPE})
    matches = []
    for group in groups:
        matches.extend(get_match_by_group(group))
    return matches


def get_match_by_group(group):
    country = group.find(TEAM_HTML_ATTRIBUTE, {"class": GROUP_COUNTY_CLASS})
    tournament = group.find(TEAM_HTML_ATTRIBUTE, {
                            "class": GROUP_TOURNAMENT_CLASS})
    match_parts = group.findAll("tr", {"id": lambda L: L})
    home_teams = match_parts[::2]
    away_teams = match_parts[1::2]
    group_matches = []
    for i in range(min(len(home_teams), len(away_teams))):
        group_matches.append(get_all_match(home_teams[i], away_teams[i]))
    return group_matches


def get_all_match(home, away):
    data = {}
    data["home_name"] = home.find(
        TEAM_HTML_ATTRIBUTE, {"class": TEAM_NAME_CLASS}).text
    data["away_name"] = away.find(
        TEAM_HTML_ATTRIBUTE, {"class": TEAM_NAME_CLASS}).text
    data["score"] = home.find(
        "td", {"class": lambda L: HOME_SCORE_CLASS in L}).text
    data["score"] += ":" + \
        away.find("td", {"class": lambda L: AWAY_SCORE_CLASS in L}).text
    data["time"] = home.find("td", {"class": lambda L: "time" in L}).text
    data["id"] = home["id"].split("_")[-1]
    return data


def get_nested_info(id):
    data = {}
    try:
        raw = make_soup(BASE_URL + GAME_SESSION_NAME + id + NESTED_GAME_URL) 
        data["mutual_last_matches"] = table_search("head_to_head h2h_mutual", raw)
        raw1 = make_soup(BASE_URL + GAME_SESSION_NAME + id + NESTED_HOME)
        data["home_last_matches"] = table_search("head_to_head h2h_home", raw1)
        raw2 = make_soup(BASE_URL + GAME_SESSION_NAME + id + NESTED_AWAY)
        data["away_last_matches"] = table_search("head_to_head h2h_away", raw2)
        return data
    except:
        return {}


def table_search(html_class_name, raw_soup):
    table = raw_soup.find("table", {"class": html_class_name})
    previous_matches_data = []
    for match in table.find("tbody"):
        match = list(match)
        if len(match) >= 5:
            previous_matches_data.append({"date": match[0].text,
                                          "league": match[1].text,
                                          "home": match[2].text,
                                          "away": match[3].text,
                                          "score": match[4].text})
    return previous_matches_data


if __name__ == "__main__":
    with open("src.json", "w") as file:
        json.dump(get_nested_info(sys.argv[1]), file)
