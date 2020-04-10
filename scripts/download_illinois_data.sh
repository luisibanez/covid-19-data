#!/bin/bash

curl -X GET http://www.dph.illinois.gov/sitefiles/COVIDZip.json?nocache=1 --output ../data/United_States/Illinois/COVIDZip.json

curl -X GET http://www.dph.illinois.gov/sitefiles/COVIDHistoricalTestResults.json?nocache=1 --output ../data/United_States/Illinois/COVIDHistoricalTestResults.json
