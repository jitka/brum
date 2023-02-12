import requests
import os
from pprint import pprint

token = os.environ['GOLEMIO_KEY']

headers = {
    'accept': 'application/json',
    'X-Access-Token': token,
}

params = {
    'limit': '1000',
    'offset': '0',
}

url = 'https://api.golemio.cz/v2'

response = requests.get(url + '/gtfs/stops', headers=headers, params={'names': 'Palmovka'})
palmovka_stops = response.json()['features']
palmovka_stops_ids = [stop['properties']['stop_id'] for stop in palmovka_stops]

response = requests.get(url + '/pid/departureboards', headers=headers, params={
    'names': 'Palmovka',
    'mitutesBefore': 0,
    'minutesAfter': 60,
    'limit': 100,
    'filter': 'routeHeadingOnce',
    })


departures = response.json()['departures']

for departure in departures:
    print(departure['route']['short_name'], departure['trip']['headsign'], departure['departure_timestamp']['predicted'])

#pprint(hui)
