#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/COVIDZip.json', 'r') as file:
    covid_dict = json.load(file)

last_update = covid_dict['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))

zip_values = covid_dict['zip_values']
zip_columns = ['zip','confirmed_cases']


#
#  Export the number of confirmed cases by ZIP
#
csv_filename = '../data/United_States/Illinois/confirmed_cases_by_zip.csv'

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=zip_columns)
        writer.writeheader()
        for data in zip_values:
            row = { 'zip': data['zip'], 'confirmed_cases': data['confirmed_cases'] }
            writer.writerow(row)

except IOError:
    print("I/O error")

