1. Issue: Permission Denied Error

Details: When integrating GitHub with Jenkins and Jira, an error occurs when attempting to create an issue in Jira. The error message returned is:

```bash
{"errorMessages":["You do not have permission to create issues in this project."],"errors":{}}
```
This indicates that the Jira API token or user account lacks the necessary permissions. Additionally, when trying to trigger issue creation with a comment tagged /jira, the integration fails, but untagged comments trigger the event correctly.

Solution: The error occurred because the Jira user account did not have sufficient permission to create issues in the specified project. To resolve this, I provided the necessary permissions to the user account in Jira. After assigning the appropriate permissions, the issue creation and comment tagging functioned as expected.         

2. Issue:
Error: "Specify a valid project ID or key"

Details:
The system is unable to recognize the provided project ID or key.

```bash
{
    "errorMessages": [],
    "errors": {
        "project": "Specify a valid project ID or key"
    }
}
```
Solution: To resolve this issue, I created two scripts: issue_types.py and list_of_jira_project.py. These scripts list all available projects along with their project IDs and keys. After running these scripts, I identified the correct project key. In my case, I selected the default key type "epic," which resolved the problem.

