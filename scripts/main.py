from RESTClientUtil import RESTClientUtil
from Constants import *
import requests.exceptions as re

if __name__ == '__main__':

    restClient = RESTClientUtil()
    try:
        # calling GET method [fetching the info of an issue]
        response_get = restClient.get(GET_URL, HEADERS, AUTH)
        print('Success!, issue fetched', response_get.status_code, '-', response_get.reason)
        data = response_get.json()
        # writing issue data into a file
        with open('issue_info.txt', 'w') as file:
            file. write('Issue description: ' + data['fields']['issuetype']['description'] + '\n')
            file.write('Issue Type: ' + data['fields']['issuetype']['name'] + '\n')
            file.write('Assignee: ' + data['fields']['assignee']['emailAddress'] + '\n')
            file.write('Reporter: ' + data['fields']['reporter']['emailAddress'] + '\n')
            file.write('Sprint: ' + data['fields']['customfield_10020'][0]['name'] + '\n')
            file.write('Priority: ' + data['fields']['priority']['name'] + '\n')
            file.write('Status: ' + data['fields']['status']['name'] + '\n')
        response_get.raise_for_status()

        # calling POST method [creating an issue]
        payload_data = restClient.payload_post_data
        response_post = restClient.post(POST_URL, HEADERS, AUTH, payload_data)
        print('Success!, issue created', response_post.status_code, '-', response_post.reason)
        response_post.raise_for_status()

        # calling PUT method [updating an issue]
        payload_data = restClient.payload_put_data
        response_put = restClient.put(PUT_URL, HEADERS, AUTH, payload_data)
        print('Success!, issue updated', response_put.status_code, '-', response_put.reason)
        response_put.raise_for_status()

        # calling DELETE method [deleting an issue]
        response_delete = restClient.delete(DELETE_URL, HEADERS, AUTH)
        print('Success!, issue deleted', response_delete.status_code, '-', response_delete.reason)
        response_delete.raise_for_status()

    except re.HTTPError as error:
        print('Error!!', error, sep='\n')
    except re.ConnectionError as error:
        print('Connection Error!!', error, sep='\n')
    except re.InvalidURL as error:
        print('Error!!', error, sep='\n')
    except re.Timeout as error:
        print('Error!!', error, sep='\n')
    except re.RequestException as error:
        print('Error!!', error, sep='\n')
