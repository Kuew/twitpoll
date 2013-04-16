#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

parties = {
    "Conservatives": {"name": "Conservative Party", "abbr": "CON", "color": "#0086DC"},
    "WelshConserv": {"name": "Conservative Party", "abbr": "CON", "color": "#0086DC"},
    "ScotTories": {"name": "Conservative Party", "abbr": "CON", "color": "#0086DC"},
    "NI_Conservative": {"name": "Conservative Party", "abbr": "CON", "color": "#0086DC"},

    "UKLabour": {"name": "Labour Party", "abbr": "LAB", "color": "#B70504"},
    "welshlabour": {"name": "Labour Party", "abbr": "LAB", "color": "#B70504"},
    "scottishlabour": {"name": "Labour Party", "abbr": "LAB", "color": "#B70504"},
    "LabourPartyNI": {"name": "Labour Party", "abbr": "LAB", "color": "#B70504"},

    "LibDems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "WelshLibDems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "scotlibdems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "libdemsni": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},

    "TheGreenParty": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},
    "WalesGreenParty": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},
    "scotgp": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},
    "GreenPartyNI": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},

    "UKIP": {"name": "UK Independence Party", "abbr": "UKIP", "color": "#A54396"},
    "ukipwales": {"name": "UK Independence Party", "abbr": "UKIP", "color": "#A54396"},
    "ukipscotland": {"name": "UK Independence Party", "abbr": "UKIP", "color": "#A54396"},

    "bnp": {"name": "British National Party", "abbr": "BNP", "color": "#854B0C"},

    "RespectPartyUK": {"name": "Respect Party", "abbr": "RES", "color": "#555555"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

