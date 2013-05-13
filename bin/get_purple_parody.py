#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

parties = {
    "UKIP": {"name": "UK Independence Party", "abbr": "UKIP", "color": "#A54396"},
    "UpikTips": {"name": "UpikTips", "abbr": "TIPS", "color": "#F1E830"},
}

uri = "https://api.twitter.com/1/users/lookup.json?screen_name=" + ",".join(parties.keys())
for party in requests.get(uri).json():
    screen_name = party["screen_name"]
    parties[screen_name]["user"] = party

sys.stdout.write(json.dumps(parties))

