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



#
#  Export the number of confirmed cases by ZIP per age group
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_zip_per_age.csv'

age_columns = ['Zip', 'Unknown', '<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=age_columns)
        writer.writeheader()
        for zip_data in zip_values:
            age_data = zip_data['demographics']['age']
            age_row = { 'Zip': zip_data['zip'] }
            for age_entry in age_data:
                age_row[age_entry['age_group']] = age_entry['count']
            writer.writerow(age_row)

except IOError:
    print("I/O error")

