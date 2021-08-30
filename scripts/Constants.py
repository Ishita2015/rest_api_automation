from requests.auth import HTTPBasicAuth

TEST_END_POINT = "https://ishitanigam.atlassian.net/rest/api/2/issue/"
GET_URL = "https://ishitanigam.atlassian.net/rest/api/2/issue/APIAUTO-1"
POST_URL = "https://ishitanigam.atlassian.net/rest/api/2/issue"
PUT_URL = "https://ishitanigam.atlassian.net/rest/api/2/issue/APIAUTO-8"
DELETE_URL = "https://ishitanigam.atlassian.net/rest/api/2/issue/APIAUTO-5"
AUTH = HTTPBasicAuth(os.environ.get('rest_api_user'), os.environ.get('rest_api_key'))
DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json"
}
