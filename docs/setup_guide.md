# Setup Guide - AI Meeting Presentation Agent (n8n)

Follow these steps to deploy and configure the n8n-native meeting automation.

## 1. Environment Setup
- **n8n Instance**: Ensure you have access to an n8n instance (Cloud or Self-hosted).
- **Google Cloud Console**:
  - Create a project and enable the **Google Slides API** and **Google Drive API**.
  - Configure **OAuth2 Credentials** or a **Service Account**.
- **OpenAI**: Generate an API key from the [OpenAI Platform](https://platform.openai.com/).

## 2. Import Workflow
1. Download the `workflow/meeting_to_slides_n8n.json` from this repository.
2. In n8n, click on **Workflows** > **Import from File**.
3. Select the downloaded JSON.

## 3. Configure Credentials
In your n8n credentials manager, add the following:
- **Google OAuth2 / Service Account**: Connect your Google account.
- **OpenAI API**: Add your OpenAI API key.

## 4. Map Variables
1. Open the **Set Transcript Input** node and paste your meeting transcript.
2. Update the **Template ID** in the logic node (or Variable node) with your specific Google Slides Template ID: `1vXhzzhoypMD2V5ayDzN0IB5RybMcGVAEx8XIoysc8qk`.
3. Ensure the Service Account email (if using one) has **Editor** access to the Google Slides Template.

## 5. Execution
- Trigger the workflow manually to test the flow.
- The system will perform Analysis -> Content Generation -> QA Check -> Slide Generation.
- Check your Google Drive for the new "Meeting Analysis Presentation" file.
