import requests


JOHN_ID = "fc617ca1-623f-4a97-9d74-270cfbeafcef"


ENDPOINT = 'http://localhost:8000/api/contacts/'


URL = ENDPOINT + ID

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    print(response.json())

