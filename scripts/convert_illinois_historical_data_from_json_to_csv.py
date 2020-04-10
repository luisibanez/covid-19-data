#!/usr/bin/env python3

import json
import csv

with open('../data/United_States/Illinois/COVIDHistoricalTestResults.json', 'r') as file:
    covid_history = json.load(file)

last_update = covid_history['LastUpdateDate']

print('Last Update Date: {}-{}-{}'.format(last_update['year'], last_update['month'], last_update['day']))



#
#  Export the state testing results
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


