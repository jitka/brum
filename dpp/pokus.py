import requests
from pprint import pprint

cookies = {
    'PHPSESSID': 'olfe47p0qi4jp1bpk6gei24jtg',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'cs,en',
    'Content-Type': 'text/json',
    'Origin': 'jitka@ucw.cz script',
    'Connection': 'keep-alive',
}

json = {
        "hash":["a9f6f07a9a85ea8e79cd8c35837cb4f2","090a7d01ef3f229abad4d4c08c73293d"],
        "linky":8,  # číslo linky
        }

response = requests.post('http://tram.mobilnitabla.cz/GETDATA/', cookies=cookies, headers=headers, json=json)


#server = 'http://tram.mobilnitabla.cz/GETDATA/'
#res = requests.get(server)
pprint(response.json()['spoje'])
