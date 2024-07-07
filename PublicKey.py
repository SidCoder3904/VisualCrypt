import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES=["https://www.googleapis.com/auth/spreadsheets"]

Spreadsheet_id="1uI8lRO2jZ-nx3wXKjRthRcSGLO9NWnOkoJlYVlAUIWE"

def GetPublicKeys():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        numberusers = sheet.values().get(spreadsheetId=Spreadsheet_id,range=f"Sheet1!B1").execute()
        numberusers = numberusers.get('values', [])
        result = sheet.values().get(spreadsheetId=Spreadsheet_id,range=f"Sheet1!A3:B{int(numberusers[0][0])+2}").execute()
        values = result.get('values', [])
        
        if not values:
            print('No data found.')
            return

        return values
    except HttpError as err:
        print(err)
def CreateUser(name,publickey):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        numberusers = sheet.values().get(spreadsheetId=Spreadsheet_id,range=f"Sheet1!B1").execute()
        numberusers = numberusers.get('values', [])
        sheet.values().update(spreadsheetId=Spreadsheet_id,range=f"Sheet1!A{int(numberusers[0][0])+3}",valueInputOption="USER_ENTERED",body={"values":[[name]]}).execute()
        sheet.values().update(spreadsheetId=Spreadsheet_id,range=f"Sheet1!B{int(numberusers[0][0])+3}",valueInputOption="USER_ENTERED",body={"values":[[publickey]]}).execute()
        sheet.values().update(spreadsheetId=Spreadsheet_id,range=f"Sheet1!B1",valueInputOption="USER_ENTERED",body={"values":[[int(numberusers[0][0])+1]]}).execute()
    except HttpError as err:
        print(err)

