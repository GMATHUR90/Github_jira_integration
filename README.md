# GitHub-Jira Integration

This Python project provides a seamless integration between GitHub and Jira, automatically creating Jira tickets whenever a comment is made on an issue in a GitHub repository. This integration is designed to improve workflow efficiency and ensure that all comments on GitHub issues are tracked and managed in Jira.

## Features

- **Comment Monitoring**: Automatically monitors comments on GitHub issues.
- **Jira Ticket Creation**: Creates a new Jira ticket whenever a comment is detected on a GitHub issue.
- **Configurable Mapping**: Easily configure which GitHub repositories and Jira projects are linked.
- **Secure Authentication**: Uses OAuth and API tokens to securely communicate between GitHub and Jira.
- **Detailed Logging**: Provides comprehensive logs to track the integration's performance and troubleshoot issues.

## Prerequisites

Before setting up the integration, ensure you have the following:

- Python 3.7 or later
- GitHub account with access to the relevant repositories
- Jira account with API access
- Git installed on your machine

## Installation

### Clone the Repository:

```bash
git clone https://github.com/yourusername/github-jira-integration.git
cd github-jira-integration
```
### Install Dependencies:
```bash
pip install -r requirements.txt
```
## Set Up Environment Variables:
1.Create a .env file in the root directory of the project.
2. Add your GitHub and Jira credentials to the .env file:
```bash
GITHUB_TOKEN=your_github_token
JIRA_API_TOKEN=your_jira_api_token
JIRA_USERNAME=your_jira_username
JIRA_PROJECT_KEY=your_jira_project_key
```
## Run the Integration:
```bash
python main.py
```


