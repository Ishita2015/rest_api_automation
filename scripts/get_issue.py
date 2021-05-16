import requests
from requests.auth import HTTPBasicAuth
import json
from scripts.Constants import *
import os


#api_key = os.environ.get('rest_api_key')
#api_user = os.environ.get('rest_api_user')

auth = HTTPBasicAuth("ishita.nigam@outlook.com", "GWqitVShMZctbXrFdluaCF1A")

headers = {
    "Accept": "application/json"
}

response = requests.get(
    url='https://ishitanigam.atlassian.net/rest/api/2/issue/APIAUTO-1',
    headers=headers,
    auth=auth
)
print((response.text))
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# print(json.dumps(json.loads(str(response.json)), sort_keys=True, indent=4, separators=(",", ": ")))
