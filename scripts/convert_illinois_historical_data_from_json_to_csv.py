#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/COVIDHistoricalTestResults.json', 'r') as file:
    covid_history = json.load(file)

last_update = covid_history['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))



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

county_columns = ['testDate', 'County', 'total_tested', 'confirmed_cases', 'deaths', 'negative']

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
                writer.writerow(county_row)

except IOError:
    print("I/O error")


