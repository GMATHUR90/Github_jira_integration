import requests
from requests.auth import HTTPBasicAuth
import os
import json

# Jira credentials (ensure these environment variables are set)
email_id = os.getenv('EMAIL_ID')  # Your Jira email
jira_api_token = os.getenv('JIRA_API_TOKEN')  # Your Jira API token
auth = HTTPBasicAuth(email_id, jira_api_token)

# Jira API endpoint to get all projects
url = "https://ecegauravmathur90-1724568897886.atlassian.net/rest/api/3/project"

# Set headers
headers = {
    "Accept": "application/json"
}

# Make the GET request to fetch projects
response = requests.get(url, headers=headers, auth=auth)

# Parse the JSON response
projects = response.json()
print(projects)

# Pretty print the project details
print(json.dumps(projects, indent=4, sort_keys=True))

