#!/usr/bin/python

#https://www.trafiklab.se/api
#filip.stenbeck@hotmail.com
import urllib2
import json
from sl_lib import *

#keys
search_string = 'uppsala centralstation'

#Id's
Uppsala = get_place_id('Uppsalacentralstation')
Stockholm = get_place_id('StockholmsCentralstation')

jam_error = is_jam('tram','38')
print( jam_error )
if not jam_error:
    trip_list = next_trips( Uppsala, Stockholm )
    for item in trip_list:
        print item.o_t
else:
    print( jam_error )







