import requests
from requests.auth import HTTPBasicAuth
import json

from flask import Flask

# Creating a flask app instance
app = Flask(__name__)

@app.route('/creteJira', methods=['POST'])
#def hello():
#    return "Hello World"
#app.run('0.0.0.0')
def createJIRA():
  url = "https://ecegauravmathur90.atlassian.net/rest/api/3/issue"
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

  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
  )

  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  


