#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/COVIDZip.json', 'r') as file:
    covid_dict = json.load(file)

last_update = covid_dict['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))

zip_values = covid_dict['zip_values']




#
#  Export the number of confirmed cases by ZIP
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_zip.csv'

zip_columns = ['zip', 'confirmed_cases']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=zip_columns)
        writer.writeheader()
        for zip_data in zip_values:
            zip_row = { 'zip': zip_data['zip'], 'confirmed_cases': zip_data['confirmed_cases'] }
            writer.writerow(zip_row)

except IOError:
    print("I/O error")




#
#  Export the number of confirmed cases by ZIP per gender
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_zip_per_gender.csv'

gender_columns = ['Zip', 'Male', 'Female', 'Unknown/Left Blank']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=gender_columns)
        writer.writeheader()
        for zip_data in zip_values:
            gender_data = zip_data['demographics']['gender']
            gender_row = { 'Zip': zip_data['zip'], 'Male': 0, 'Female': 0, 'Unknown/Left Blank': 0 }
            for gender_entry in gender_data:
                gender_row[gender_entry['description']] = gender_entry['count']
            writer.writerow(gender_row)

except IOError:
    print("I/O error")

