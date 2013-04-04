#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

parties = {
    "ConsFuture": {"name": "Conservative Future", "abbr": "CON", "color": "#0086DC"},
    "YoungLabourUK": {"name": "Young Labour", "abbr": "LAB", "color": "#B70504"},
    "liberalyouth": {"name": "Liberal Youth", "abbr": "LD", "color": "#FDBB30"},
    "YoungGreenParty": {"name": "Young Greens", "abbr": "GP", "color": "#6AB023"},
    "SNPyouth": {"name": "The YSI (SNP)", "abbr": "SNP", "color": "#FFF95D"},
    "YIofficial": {"name": "Young Independence (UKIP)", "abbr": "UKIP", "color": "#A54396"},
    "SF_RY": {"name": "Sinn Féin Republican Youth", "abbr": "SF", "color": "#00857D"},
    "plaidifancyouth": {"name": "Plaid Ifanc Youth", "abbr": "PLAID", "color": "#3F8428"},
    #"duponline": {"name": "Democratic Unionist Party", "abbr": "DUP", "color": "#E7E7E8"},
    #"allianceparty": {"name": "Alliance Party", "abbr": "ALL", "color": "#000000"},
    #"SDLPlive": {"name": "Social Democratic and Labour Party", "abbr": "SDLP", "color": "#007450"},
    #"uuponline": {"name": "Ulster Unionist Party", "abbr": "UUP", "color": "#A0CEF2"},
    #"bnp": {"name": "British National Party", "abbr": "BNP", "color": "#854B0C"},
    #"scotgp": {"name": "Scottish Green Party", "abbr": "SGP", "color": "#92D400"},
    #"GreenPartyNI": {"name": "Green Party in Northern Ireland", "abbr": "GPNI", "color": "#3053B3"},
    #"RespectPartyUK": {"name": "Respect Party", "abbr": "RES", "color": "#555555"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

