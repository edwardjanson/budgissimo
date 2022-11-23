from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import os

from api_helpers import *


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
RANGE_NAME = 'Sheet1!A:E'
SERVICE_ACCOUNT_FILE = 'api_connections/service_account.json'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=credentials)

        read_sheet(service, SPREADSHEET_ID, RANGE_NAME)

        values = [
            ['A', 'B'],
            ['C', 'D']
        ]

        write_sheet(service, values, SPREADSHEET_ID, RANGE_NAME)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()