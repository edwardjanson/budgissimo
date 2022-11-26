from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from api_connections.api_helpers import read_sheet, write_sheet

import os


SCOPES = ["https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

SERVICE_ACCOUNT_FILE = "api_connections/service_account.json"


def run_gs_api(platform, request, account):
    RANGE_NAME = f"{platform.name}!A:G"
    SPREADSHEET_ID = account.spreadsheet_id
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build("sheets", "v4", credentials=credentials)

        if request == "read":
            read_sheet(service, SPREADSHEET_ID, RANGE_NAME, platform)
        elif request == "write":
            write_sheet(service, SPREADSHEET_ID, RANGE_NAME, platform)

    except HttpError as err:
        print(err)