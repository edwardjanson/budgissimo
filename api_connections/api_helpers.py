from models.budget import Budget
from models.platform import Platform


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


def data_by_rows(platform_campaigns):
    data_by_rows = []
    sheet_headers = []

    for attribute, value in platform_campaigns[0].__dict__.items():
        if attribute != "id":
                sheet_headers.append(attribute)
    
    data_by_rows.append(sheet_headers)
    
    for campaign in platform_campaigns:
        cell_values = []
        for attribute, value in campaign.__dict__.items():
            if attribute != "id":
                if type(value) is Budget:
                    cell_values.append(value.monthly_budget)
                elif type(value) is Platform:
                    cell_values.append(value.name)
                else:
                    cell_values.append(value)

        data_by_rows.append(cell_values)


    return data_by_rows
