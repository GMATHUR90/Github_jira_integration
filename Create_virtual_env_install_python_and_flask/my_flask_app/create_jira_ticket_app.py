# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():
    # Get the comment from request payload
    data = request.get_json() 
    comment = data.get('comment', '') # Assuming comment is part of payload
    url = "https://ecegauravmathur90-1724568897886.atlassian.net/rest/api/3/issue"

    email_id = os.getenv('EMAIL_ID')
    jira_api_token = os.getenv('JIRA_API_TOKEN')
    auth = HTTPBasicAuth(email_id, jira_api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "SCRUM"
        },
        "issuetype": {
            "id": "10004"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    # Check if the comment contains /jira

    if '/jira' in comment:
        response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                auth=auth
    )
    
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    # If /jira is not found, return a message
    return json.dumps({"message":"Comment does not contain /jira"}, sort_keys=True, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
