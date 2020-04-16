#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/CountyDemos.json', 'r') as file:
    covid_dict = json.load(file)

last_update = covid_dict['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))

county_values = covid_dict['county_demographics']




#
#  Export the number of confirmed cases by County
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_county.csv'

county_columns = ['County', 'confirmed_cases']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=county_columns)
        writer.writeheader()
        for county_data in county_values:
            county_row = { 'County': county_data['County'], 'confirmed_cases': county_data['confirmed_cases'] }
            writer.writerow(county_row)

except IOError:
    print("I/O error")




#
#  Export the number of confirmed cases by County per gender
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_county_per_gender.csv'

gender_columns = ['County', 'Male', 'Female', 'Unknown/Left Blank']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=gender_columns)
        writer.writeheader()
        for county_data in county_values:
            gender_data = county_data['demographics']['gender']
            gender_row = { 'County': county_data['County'], 'Male': 0, 'Female': 0, 'Unknown/Left Blank': 0 }
            for gender_entry in gender_data:
                gender_row[gender_entry['description']] = gender_entry['count']
            writer.writerow(gender_row)

except IOError:
    print("I/O error")



#
#  Export the number of confirmed cases by County per age group
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_county_per_age.csv'

age_columns = ['County', 'Unknown', '<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=age_columns)
        writer.writeheader()
        for county_data in county_values:
            age_data = county_data['demographics']['age']
            age_row = { 'County': county_data['County'] }
            for age_entry in age_data:
                age_row[age_entry['age_group']] = age_entry['count']
            writer.writerow(age_row)

except IOError:
    print("I/O error")



#
#  Export the number of confirmed cases by County per race
#

csv_filename = '../data/United_States/Illinois/confirmed_cases_by_county_per_race.csv'

race_columns = ['County', 'White', 'Black', 'Left Blank', 'Other', 'Asian', 'Hispanic', 'NH/PI*', 'AI/AN**']


try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=race_columns)
        writer.writeheader()
        for county_data in county_values:
            race_data = county_data['demographics']['race']
            race_row = { 'County': county_data['County'] }
            for race_entry in race_data:
                race_row[race_entry['description']] = race_entry['count']
            writer.writerow(race_row)

except IOError:
    print("I/O error")

