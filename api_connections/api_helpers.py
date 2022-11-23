def read_sheet(service, spreadsheet_id, range_name):
    result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()

    rows = result.get('values', [])
    print(f"{len(rows)} rows retrieved")

    for row in rows:
        # Print columns A and E, which correspond to indices 0 and 4.
        # print('%s, %s' % (row[0], row[4]))
        print('%s' % (row[0]))

    return rows


def write_sheet(service, values, spreadsheet_id, range_name):
        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption="USER_ENTERED", body=body).execute()

        print(f"{result.get('updatedCells')} cells updated.")

        return result