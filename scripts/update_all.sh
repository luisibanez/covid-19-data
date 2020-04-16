#!/bin/bash

ILLINOIS_REPO="${HOME}/data/covid-19-illinois-data/"
DATA_DIR="${HOME}/data/covid-19-data/data/United_States/Illinois"


#
#  Download data from Illinois Department of Public Health.
#
./download_illinois_data.sh


#
#  Convert JSON data into CSV file.
#
./convert_illinois_data_per_county_from_json_to_csv.py
./convert_illinois_data_per_zip_from_json_to_csv.py
./convert_illinois_historical_data_from_json_to_csv.py


#
#  Update local repository and its remote in Github.
#
git checkout data_imports
git pull origin master
git add ../data
git commit -m "Update data to $(date +%F)."

git checkout master
git merge --no-ff data_imports

#
#  Update remote repository in Github.
#
git push origin master


#
#  Update "covid-19-illinois-data" repository
#
cd "${ILLINOIS_REPO}"
cp "${DATA_DIR}/*.csv" "${ILLINOIS_REPO}"
git pull origin master
git add ./*.csv
git commit -m "Update data to $(date +%F)."
git push origin master

