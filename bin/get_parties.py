#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

parties = {
    "Conservatives": {"name": "Conservative Party", "abbr": "CON", "color": "#0086DC"},
    "UKLabour": {"name": "Labour Party", "abbr": "LAB", "color": "#B70504"},
    "LibDems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "TheGreenParty": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},
    "theSNP": {"name": "Scottish National Party", "abbr": "SNP", "color": "#FFF95D"},
    "UKIP": {"name": "UK Independence Party", "abbr": "UKIP", "color": "#A54396"},
    "sinnfeinireland": {"name": "Sinn Féin", "abbr": "SF", "color": "#00857D"},
    "Plaid_Cymru": {"name": "Plaid Cyrmu", "abbr": "PLAID", "color": "#3F8428"},
    #"JimAllister": {"name": "Traditional Unionist Voice", "abbr": "TUV", "color": "#23116F"},
    "duponline": {"name": "Democratic Unionist Party", "abbr": "DUP", "color": "#E7E7E8"},
    "allianceparty": {"name": "Alliance Party", "abbr": "ALL", "color": "#000000"},
    "SDLPlive": {"name": "Social Democratic and Labour Party", "abbr": "SDLP", "color": "#007450"},
    "uuponline": {"name": "Ulster Unionist Party", "abbr": "UUP", "color": "#A0CEF2"},
    "bnp": {"name": "British National Party", "abbr": "BNP", "color": "#854B0C"},
    "scotgp": {"name": "Scottish Green Party", "abbr": "SGP", "color": "#92D400"},
    "GreenPartyNI": {"name": "Green Party in Northern Ireland", "abbr": "GPNI", "color": "#3053B3"},
    "RespectPartyUK": {"name": "Respect Party", "abbr": "RES", "color": "#555555"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

