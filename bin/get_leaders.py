#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

leaders = {
    "David_Cameron": {"name": "David Cameron", "abbr": "CON", "color": "#0086DC"},
    "Ed_Miliband": {"name": "Ed Miliband", "abbr": "LAB", "color": "#B70504"},
    "nick_clegg": {"name": "Nick Clegg", "abbr": "LD", "color": "#FDBB30"},
    "natalieben": {"name": "Natalie Bennett", "abbr": "GP", "color": "#6AB023"},
    "AlexSalmond": {"name": "Alex Salmond", "abbr": "SNP", "color": "#FFF95D"},
    "Nigel_Farage": {"name": "Nigel Farage", "abbr": "UKIP", "color": "#A54396"},
    "GerryAdamsSF": {"name": "Gerry Adams", "abbr": "SF", "color": "#00857D"},
    "LeanneWood": {"name": "Leanne Wood", "abbr": "PLAID", "color": "#3F8428"},
    "JimAllister": {"name": "Jim Allister", "abbr": "TUV", "color": "#23116F"},
    "DUPleader": {"name": "Peter Robinson", "abbr": "DUP", "color": "#E7E7E8"},
    "AlasdairMcD_MP": {"name": "Alasdair McDonnell", "abbr": "SDLP", "color": "#007450"},
    "mikenesbittni": {"name": "Mike Nesbitt", "abbr": "UUP", "color": "#A0CEF2"},
    "nickgriffinmep": {"name": "Nick Griffin", "abbr": "BNP", "color": "#854B0C"},
    "StevenAgnew": {"name": "Steven Agnew", "abbr": "GPNI", "color": "#3053B3"},
    "georgegalloway": {"name": "George Galloway", "abbr": "RES", "color": "#555555"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(leaders.keys())
for leader in requests.get(uri).json():
    screen_name = leader["screen_name"]
    leaders[screen_name]["user"] = leader

sys.stdout.write(json.dumps(leaders))

