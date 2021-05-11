import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ishitanigam.atlassian.net/rest/api/2/issue/APIAUTO-1"
auth = HTTPBasicAuth("ishita.nigam@outlook.com", "GWqitVShMZctbXrFdluaCF1A")

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
