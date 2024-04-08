from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import io

# Step 1: Read URLs from the Spreadsheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("bpt-files-71f8d02803dc.json", scope)
client = gspread.authorize(creds)

# Authenticate with the Google Drive API
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/drive.file'])
creds = flow.run_local_server(port=0)
service = build('drive', 'v3', credentials=creds)


folder_id = '1-HD8Og9CPtTLlyz3EfImHOQ9EMLeZx9G'
for filename in os.listdir('./downloads'):
    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    media = MediaFileUpload("./downloads/" + filename, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))

    # Clean up by removing files after upload
    os.remove("./downloads/" + filename)