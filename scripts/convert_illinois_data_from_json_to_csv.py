#!/usr/bin/env python3

import json

with open('../data/United_States/Illinois/COVIDZip.json', 'r') as file:
    covid_dict = json.load(file)

last_update = covid_dict['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))
