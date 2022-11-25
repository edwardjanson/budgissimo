from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from api_connections.api_helpers import read_sheet, write_sheet, data_by_rows
import repositories.platform_repository as platform_repository
import repositories.campaign_repository as campaign_repository

import os


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
RANGE_NAME = 'Sheet1!A:G'
SERVICE_ACCOUNT_FILE = 'api_connections/service_account.json'


def run_gs_api(platform, request):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=credentials)

        if request == "read":
            read_sheet(service, SPREADSHEET_ID, RANGE_NAME)
        elif request == "write":
            platform_data = data_by_rows(platform)
            write_sheet(service, platform_data, SPREADSHEET_ID, RANGE_NAME)

    except HttpError as err:
        print(err)