#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/COVIDHistoricalTestResults.json', 'r') as file:
    covid_history = json.load(file)

last_update = covid_history['LastUpdateDate']

last_update_string = '{}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day'])
print('Last Update Date: {}'.format(last_update_string))



#
#  Export the state testing historical results
#

csv_filename = '../data/United_States/Illinois/historical_state_testing_results.csv'

state_testing_results = covid_history['state_testing_results']['values']

state_columns = ['testDate', 'total_tested', 'confirmed_cases', 'deaths']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=state_columns)
        writer.writeheader()
        for daily_results in state_testing_results:
            writer.writerow(daily_results)

except IOError:
    print("I/O error")



#
#  Export the state testing historical results by county
#

csv_filename = '../data/United_States/Illinois/historical_state_testing_results_by_county.csv'

historical_county = covid_history['historical_county']['values']

county_columns = ['testDate', 'County', 'total_tested', 'confirmed_cases', 'deaths', 'negative', 'lat', 'lon']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=county_columns)
        writer.writeheader()
        for daily_results in historical_county:
            county_row = { 'testDate' : daily_results['testDate'] }
            county_values = daily_results['values']
            for value in county_values:
                county_row['County'] = value['County']
                county_row['confirmed_cases'] = value['confirmed_cases']
                county_row['total_tested'] = value['total_tested']
                county_row['negative'] = value['negative']
                county_row['deaths'] = value['deaths']
                if 'lat' in value:
                    county_row['lat'] = value['lat']
                else:
                    county_row['lat'] = 0.0
                if 'lon' in value:
                    county_row['lon'] = value['lon']
                else:
                    county_row['lon'] = 0.0
                writer.writerow(county_row)

except IOError:
    print("I/O error")



#
#  Export the state characteristics by county
#

csv_filename = '../data/United_States/Illinois/characteristics_by_county.csv'

characteristics_by_county = covid_history['characteristics_by_county']['values']

county_columns = ['County', 'last_update', 'total_tested', 'confirmed_cases', 'deaths', 'negative', 'lat', 'lon']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=county_columns)
        writer.writeheader()
        county_row = { 'last_update' : last_update_string }
        for county in characteristics_by_county:
              county_row['County'] = county['County']
              county_row['confirmed_cases'] = county['confirmed_cases']
              county_row['total_tested'] = county['total_tested']
              county_row['negative'] = county['negative']
              county_row['deaths'] = county['deaths']
              if 'lat' in county:
                  county_row['lat'] = county['lat']
              else:
                  county_row['lat'] = 0.0
              if 'lon' in county:
                  county_row['lon'] = county['lon']
              else:
                  county_row['lon'] = 0.0
              writer.writerow(county_row)

except IOError:
    print("I/O error")


#
#  Export the state characteristics by age
#

csv_filename = '../data/United_States/Illinois/characteristics_by_age.csv'

characteristics_by_age = covid_history['demographics']['age']

age_columns = ['last_update', 'age_group', 'count', 'deaths']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=age_columns)
        writer.writeheader()
        age_row = { 'last_update' : last_update_string }
        for age_group in characteristics_by_age:
            age_row['age_group'] = age_group['age_group']
            age_row['count'] = age_group['count']
            age_row['deaths'] = age_group['deaths']
            writer.writerow(age_row)

except IOError:
    print("I/O error")


#
#  Export the state characteristics by gender
#

csv_filename = '../data/United_States/Illinois/characteristics_by_gender.csv'

characteristics_by_gender = covid_history['demographics']['gender']

gender_columns = ['last_update', 'description', 'count', 'deaths']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=gender_columns)
        writer.writeheader()
        gender_row = { 'last_update' : last_update_string }
        for gender in characteristics_by_gender:
            gender_row['description'] = gender['description']
            gender_row['count'] = gender['count']
            gender_row['deaths'] = gender['deaths']
            writer.writerow(gender_row)

except IOError:
    print("I/O error")



#
#  Export the state characteristics by race
#

csv_filename = '../data/United_States/Illinois/characteristics_by_race.csv'

characteristics_by_race = covid_history['demographics']['race']

race_columns = ['last_update', 'description', 'count', 'deaths']

try:
    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=race_columns)
        writer.writeheader()
        race_row = { 'last_update' : last_update_string }
        for race in characteristics_by_race:
            race_row['description'] = race['description']
            race_row['count'] = race['count']
            race_row['deaths'] = race['deaths']
            writer.writerow(race_row)

except IOError:
    print("I/O error")

