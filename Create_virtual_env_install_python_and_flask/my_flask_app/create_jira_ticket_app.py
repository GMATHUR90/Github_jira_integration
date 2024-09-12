from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJIRA():
    data = request.json
    comment_body = data.get('comment', {}).get('body', '')

    if '/jira' in comment_body:
        url = "https://ecegauravmathur90.atlassian.net/rest/api/3/issue"
        email_id = os.getenv('EMAIL_ID')
        jira_api_token = os.getenv('JIRA_API_TOKEN')
        auth = HTTPBasicAuth(email_id, jira_api_token)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
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
        })

        response = requests.post(url, data=payload, headers=headers, auth=auth)

        return jsonify(json.loads(response.text)), response.status_code

    return jsonify({"message": "No Jira command found in the comment. No action taken."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
