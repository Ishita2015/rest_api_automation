import requests
import json

class RESTClientUtil:
    
    def get(self, GET_URL, headers, auth):
        response = None
        try:
            response = requests.get(url=GET_URL, headers=headers, auth=auth)
        except re.HTTPError as error:
            # TODO: Replace all print statements with logger
            print('Error!!', error, sep='\n')
        except re.ConnectionError as error:
            print('Connection Error!!', error, sep='\n')
        except re.InvalidURL as error:
            print('Error!!', error, sep='\n')
        except re.Timeout as error:
            print('Error!!', error, sep='\n')
        except re.RequestException as error:
            print('Error!!', error, sep='\n')
        
        return response

    # TODO: Do not make it member variable
    payload_post_data = json.dumps({

                "fields": {
                    "issuetype": {"name": "Story"},
                    "project": {"key": "APIAUTO"},
                    "priority": {"name": "Medium"},
                    "labels": ["automation"],
                    "assignee": {"emailAddress": "ishita.nigam@outlook.com"},  # not working, need to mention accountID
                    "summary": "Jira_API_auto_8",
                    "description": "Issue created using REST API",
                    "reporter": {"accountId": "609432ec539c14006adc236d"}
                }
    })

    def post(self, POST_URL, headers, auth, payload_post_data):
        response = requests.post(url=POST_URL, headers=headers, auth=auth, data=payload_post_data)
        return response

    payload_put_data = json.dumps({

        "id": "10007",
        "fields": {
            "description": "Issue created and updated using REST API",
            "assignee": {"accountId": "609432ec539c14006adc236d"}
        }
    })

    def put(self, PUT_URL, headers, auth, payload_put_data):
        response = requests.put(url=PUT_URL, headers=headers, auth=auth, data=payload_put_data)
        return response

    def delete(self, DELETE_URL, headers, auth):
        response = requests.delete(url=DELETE_URL, headers=headers, auth=auth)
        return response
