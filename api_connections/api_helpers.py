from models.budget import Budget
from models.platform import Platform
import repositories.campaign_repository as campaign_repository


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


def data_by_rows(platform):
    campaigns = campaign_repository.select_all_by_platform(platform)

    data_by_rows = []

    sheet_headers = ["Campaign Name", "Monthly Budget", "Amount Spent"]
    
    data_by_rows.append(sheet_headers)
    
    for campaign in campaigns:
        cell_values = []
        for attribute, value in campaign.__dict__.items():
            if attribute != "id":
                if type(value) is Budget:
                    cell_values.append(value.monthly_budget)
                    cell_values.append(value.amount_spent)
                elif type(value) is Platform:
                    pass
                else:
                    cell_values.append(value)

        data_by_rows.append(cell_values)


    return data_by_rows
