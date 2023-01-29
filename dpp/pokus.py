import requests
import os
from pprint import pprint

token = os.environ['GOLEMIO_KEY']

headers = {
    'accept': 'application/json',
    'X-Access-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImppdGthQHVjdy5jeiIsImlkIjoxNjU4LCJuYW1lIjpudWxsLCJzdXJuYW1lIjpudWxsLCJpYXQiOjE2NzUwMjI5ODYsImV4cCI6MTE2NzUwMjI5ODYsImlzcyI6ImdvbGVtaW8iLCJqdGkiOiJmY2MyNTI4ZS01ZmVlLTQxOTktOGM0Yi05NzI4YzgzYmJjMGQifQ.B2IiVafxUDAccjcUuNdlacedk2_v7m4LCaf2wovm8YY',
}

params = {
    'limit': '1000',
    'offset': '0',
}

url = 'https://api.golemio.cz/v2/gtfs'

response = requests.get(url + '/stops', headers=headers, params={'names': 'Palmovka'})
palmovka_stops = response.json()['features']

pprint(len(hui))
