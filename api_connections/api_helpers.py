from models.budget import Budget
from models.platform import Platform
from models.campaign import Campaign
from models.budget import Budget
import repositories.campaign_repository as campaign_repository
import repositories.budget_repository as budget_repository


def read_sheet(service, spreadsheet_id, range_name, platform):
    result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()

    rows = result.get('values', [])
    print(f"{len(rows)} rows retrieved")

    first_row = True
    for row in rows:
        if first_row:
            first_row = False
            continue
        
        try:
            campaign = campaign_repository.select_by_campaign_name(row[0], platform)
        except IndexError:
            campaign = None

        try:
            amount_spent = float(row[2])
        except IndexError:
            amount_spent = None

        if not campaign:
            budget = Budget(float(row[1]), amount_spent)
            new_budget = budget_repository.save(budget)
            new_campaign = Campaign(row[0], new_budget, platform)
            campaign_repository.save(new_campaign)
        else:
            updated_budget = Budget(float(row[1]), amount_spent, campaign.budget.id) # type: ignore
            budget_repository.update(updated_budget)


def write_sheet(service, spreadsheet_id, range_name, platform):
        request = service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id, range=range_name)
        request.execute()

        platform_data = data_by_rows(platform)

        body = {
            'values': platform_data
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption="USER_ENTERED", body=body).execute()

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