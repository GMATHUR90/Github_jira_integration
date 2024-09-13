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

        # Jira credential from environment variables
        email_id = os.getenv('EMAIL_ID')
        jira_api_token = os.getenv('JIRA_API_TOKEN')
        auth = HTTPBasicAuth(email_id, jira_api_token)

        # Jira issue details
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        # Extracting relevant details from GitHub issue (e.g., issue title and body)
        issue_title = data.get('issue', {}).get('title', 'GitHub Issue')
        issue_body = data.get('issue', {}).get('body', 'No description provided.')

        payload = json.dumps({
            "fields": {
                "summary": f"GitHub Issue: {issue_title}",
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": issue_body,
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
                }
            }
        })

        # Make the request to create the Jira issue
        try:
            response = requests.post(url, data=payload, headers=headers, auth=auth)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return jsonify({"message": "Jira issue created", "response": response.json()}), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500
    else:
        # If comment does not contain /jira, return a message that no action was taken
        return jsonify({"message": "No Jira command found in the comment. No action taken."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
