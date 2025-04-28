# Credit Onboarding Workflow Template
## How it works:
This project includes a custom credit onboarding system implemented with Abstra and Python scripts. The requester fills out a form with their personal data to apply for credit. The request is then either automatically approved or manually evaluated, depending on the individual's credit score. The system integrates with Slack to send alerts about rejected requests and with SendGrid to notify users of approved requests via email.

Integrations:
  - Slack
  - Sendgrid

To customize this template for your team and build a lot more, [book a demonstration here.](https://meet.abstra.app/demo?url=template-credit-onboarding)

![A credit onboarding workflow built in Abstra](https://github.com/user-attachments/assets/a16e8887-c7ba-4cf7-acb7-7c9812f85958)

## Initial Configuration
To use this project, some initial configurations are necessary:

1. **Python Version**: Ensure Python version 3.9 or higher is installed on your system.
2. **Integrations**: To connect to Slack, this template uses Abstra connectors. To connect, simply open your project in [Abstra Cloud Console](https://cloud.abstra.io/projects/), add the Slack connector, and authorize it.
3. **Environment Variables**:

   The following environment variables are required for both local development and online deployment:

   - `SLACK_CHANNEL_NAME`: Slack channel where the credit rejection notification will be sent
   - `SENDGRID_API_KEY`: API Token to use Sendgrid email service
   - `SENDER_EMAIL`: Email address from which the credit approval notification will be sent

    In the scripts, we assume that a credit team is involved in the credit approval process. The `.env` variable below is the email used by this team to receive the credit applications:

   - `CREDIT_TEAM_EMAIL`: Credit team email
  
   For local development, create a `.env` file at the root of the project and add the variables listed above (as in `.env.example`). For online deployment, configure these variables in your [environment settings](https://docs.abstra.io/cloud/envvars).

5. **Dependencies**: To install the necessary dependencies for this project, a `requirements.txt` file is provided. This file includes all the required libraries.

   Follow these steps to install the dependencies:

   1. Open your terminal and navigate to the project directory.
   2. Run the following command to install the dependencies from `requirements.txt`:
  
      ```sh
      pip install -r requirements.txt
      ```
6. **Access Control**: The generated form is protected by default. For local testing, no additional configuration is necessary. However, for cloud usage, you need to add your own access rules. For more information on how to configure access control, refer to the [Abstra access control documentation](https://docs.abstra.io/concepts/access-control).

7. **Local Usage**: To access the local editor with the project, use the following command:

   ```sh
      abstra editor path/to/your/project/folder/
   ```

## General Workflow:
To implement this system use the following scripts:

### Credit Request Creation:
For creating a credit request and collecting data about it, use:
  - **order_request_form.py**: Script to generate a form that collects the requester's personal information and details about the credit request.

### Credit Request Review: 
For evaluating the credit request, use:
  - **credit_engine.py**: Script to assign a grade to the request based on its details.
  - **automatic_review.py**: Script to approve the request if its score is sufficiently high.
  - **manual_review.py**: Script to generate a form that displays information about the credit request and asks the responsible team for approval or rejection.

### Credit Request Notification:
For notifing about the request approval/rejection:
  - **approval_email.py**: Script to notify the requester if the credit request has been approved.
  - **internal_notification.py**: Script to notify a Slack channel about the request rejection.

If you're interested in customizing this template to your team in under 30min, [book a customizing session here.](https://meet.abstra.app/demo?url=template-credit-onboarding)
