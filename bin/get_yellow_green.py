#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

parties = {
    "LibDems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "scotlibdems": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "libdemsni": {"name": "Liberal Democrats", "abbr": "LD", "color": "#FDBB30"},
    "TheGreenParty": {"name": "Green Party", "abbr": "GP", "color": "#6AB023"},
    "scotgp": {"name": "Green Party", "abbr": "SGP", "color": "#6AB023"},
    "GreenPartyNI": {"name": "Green Party", "abbr": "GPNI", "color": "#6AB023"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

