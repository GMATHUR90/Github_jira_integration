import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask, request, jsonify

# Creating a flask app instance
app = Flask(__name__)

@app.route('/createJira', methods=['POST'])

def createJIRA():
  # Extract the JSON payload from the github webhook
  data = request.json

  # Extract the comment from the webhook payload
  comment_body = data.get('comment', {}).get('body', '')

  # Check if the comment contains the /jira command
  if '/jira' in comment_body:
    # URL to create a new Jira Issue 
    url = "https://ecegauravmathur90.atlassian.net/rest/api/3/issue"

    # Jira credential from environment variable
    email_id = os.getenv('EMAIL_ID')
    jira_api_token = os.getenv('JIRA_API_TOKEN')
    auth = HTTPBasicAuth(email_id, jira_api_token)

    # Jira issue details
     
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
                    "text": "My first Jira Ticket",
                    "type": "text"
                }
                ],
                "type": "paragraph"
            }
            ],
            "type": "doc",
            "version": 1
         },
    
        "issuetype": {
            "id": "10007"
        },
    
    
        "project": {
            "key": "MTS"
        },
    
        "summary": "First Jira Ticket",
    
        },
        "update": {}
    } )
    # Make the request to create the Jira issue
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
     )
    # Return the Jira API response
    #return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return jsonify(json.loads(response.text)), response.status_code
  else:
    # If comment does not contain /jira returan a message no action was taken
    return jsonify({"message": "No Jira command found in the comment. No action taken."}) , 200
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  
