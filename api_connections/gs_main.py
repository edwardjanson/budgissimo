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


def run_gs_api():
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

        google_ads = platform_repository.select(1)
        google_ads_campaigns = campaign_repository.select_all_by_platform(google_ads)
        google_ads_data = data_by_rows(google_ads_campaigns)

        write_sheet(service, google_ads_data, SPREADSHEET_ID, RANGE_NAME)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    run_gs_api()