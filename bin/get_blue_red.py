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
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

