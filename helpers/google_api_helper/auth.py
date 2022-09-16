"""A module to build google api service"""

# auth.py
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_file(
    'helpers/google_api_helper/google_api_credentials.json', scopes=SCOPES)

spreadsheet_service = build('sheets', 'v4', credentials=credentials)
