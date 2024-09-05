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

### Install Dependencies:
```bash
pip install -r requirements.txt

