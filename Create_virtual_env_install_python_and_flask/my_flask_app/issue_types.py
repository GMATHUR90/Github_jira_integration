import requests
from requests.auth import HTTPBasicAuth
import os
import pprint

url = "https://ecegauravmathur90.atlassian.net/rest/api/3/issuetype"
email_id = os.getenv('EMAIL_ID')
jira_api_token = os.getenv('JIRA_API_TOKEN')

auth = HTTPBasicAuth(email_id, jira_api_token)
headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=auth)

pprint.pprint(response.json())

