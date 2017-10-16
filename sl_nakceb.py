#!/usr/bin/python

#trafiklab.se
#filip.stenbeck@hotmail.com
import urllib2
import json


#http://api.sl.se/api2/deviations.<FORMAT>?key=<DIN API NYCKEL>&transportMode=<TRANSPORTMODE>&lineNumber=<LINENUMBER>&siteId=<SITEID>&fromDate=<FROMDATE>&toDate=<TODATE>

#keys
jam_key='82749b49e54246789070473b6f3f9b55'
tabular_key='a811280c-e0ff-4860-b8d5-51d5c701c660'

#urls
jam_url='http://api.sl.se/api2/deviations.json?key=82749b49e54246789070473b6f3f9b55&transportMode=tram&lineNumber=38'

jam_obj = urllib2.urlopen(jam_url)

jam_data = json.load(jam_obj)

for item in jam_data['ResponseData']:
    print(item['ScopeElements'])
    print(item['Details'])

