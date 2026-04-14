import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class SlidesManager:
    def __init__(self, credentials_path: str = "credentials.json"):
        self.scopes = [
            'https://www.googleapis.com/auth/presentations',
            'https://www.googleapis.com/auth/drive'
        ]
        self.creds = None
        if os.path.exists(credentials_path):
            self.creds = service_account.Credentials.from_service_account_file(
                credentials_path, scopes=self.scopes)
        
    def create_presentation_from_template(self, template_id: str, title: str) -> str:
        """Copies a template presentation and returns the new presentation ID."""
        if not self.creds:
            raise Exception("Google Cloud credentials not found. Please provide credentials.json")
            
        drive_service = build('drive', 'v3', credentials=self.creds)
        copy_body = {'name': title}
        
        try:
            presentation_copy = drive_service.files().copy(
                fileId=template_id, body=copy_body).execute()
            return presentation_copy.get('id')
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def replace_placeholders(self, presentation_id: str, placeholders: dict):
        """Replaces {{PLACEHOLDERS}} in the presentation with actual content."""
        slides_service = build('slides', 'v1', credentials=self.creds)
        
        requests = []
        for placeholder, value in placeholders.items():
            requests.append({
                'replaceAllText': {
                    'replaceText': str(value),
                    'containsText': {
                        'text': placeholder,
                        'matchCase': True
                    }
                }
            })
            
        try:
            slides_service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()
            print(f"Successfully updated presentation: {presentation_id}")
        except HttpError as error:
            print(f"An error occurred during replacement: {error}")
