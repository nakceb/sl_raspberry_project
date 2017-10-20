def get_place_id( search_string ):
    #key and documentation for this api is in trafiklab.se
    import urllib2
    import json
    place_key = '8a297ea7e75345bb9027b75918a910f4'
    place_url = 'http://api.sl.se/api2/typeahead.json?key=' + place_key + '&searchstring=' + search_string + '&stationsonly=true&maxresults=1'
    place_obj = urllib2.urlopen(place_url)
    place_data = json.load(place_obj)
    
    return place_data['ResponseData'][0]['SiteId']

def is_jam( transport_mode, line_num ):
    import urllib2
    import json
    jam_key = '82749b49e54246789070473b6f3f9b55'
    jam_url = 'http://api.sl.se/api2/deviations.json?key=' + jam_key + '&transportMode=' + transport_mode + '&lineNumber=' + line_num
    jam_obj = urllib2.urlopen(jam_url)
    jam_data = json.load(jam_obj)
    if not jam_data['ResponseData']:
        return 0
    else:
        return jam_data['ResponseData'][0]['Details']

def next_trips( origin, destination ):
    import urllib2
    import json
    trip_key = 'bc5c544d26044d81873ded6470cb6497'
    trip_url = 'http://api.sl.se/api2/TravelplannerV3/trip.'+'Json' '?key=' + trip_key + '&originId=' + origin + '&destId=' + destination + '&products=1'
    trip_obj = urllib2.urlopen(trip_url)
    trip_data = json.load(trip_obj)
    trip_list = []
    for item in trip_data['Trip']:
        origin_name = item['LegList']['Leg'][0]['Origin']['name']
        destination_name = item['LegList']['Leg'][0]['Destination']['name']
        origin_time = item['LegList']['Leg'][0]['Origin']['time']
        destination_time = item['LegList']['Leg'][0]['Destination']['time']
        travel_type = item['LegList']['Leg'][0]['Product']['name']
        trip_instance = trip(origin_name, destination_name, origin_time, destination_time, travel_type)

        trip_list.append(trip_instance)
    return trip_list

class trip:
    def __init__(self, origin_name, destination_name, origin_time, destination_time, travel_type):
        self.o_n = origin_name
        self.d_n = destination_name
        self.o_t = origin_time
        self.d_t = destination_time
        self.t_t = travel_type
