from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1WpWbclQPMMG_h2oP5CvV8TcPI2ae8-EF544yX2LmB-Q'
SAMPLE_RANGE_NAME = 'Sheet1!A:E'
SERVICE_ACCOUNT_FILE = 'api/credentials.json'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call data from the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [0])

        if not values:
            print('No data found.')
            return

        print('Name:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))

        # Write data into sheets
        values = [
            ['A', 'B'],
            ['C', 'D']
        ]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
            valueInputOption="USER_ENTERED", body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
        
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()