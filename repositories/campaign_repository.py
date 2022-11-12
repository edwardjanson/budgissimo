from db.run_sql import run_sql

from models.campaign import Campaign
import repositories.budget_repository as budget_repository
import repositories.platform_repository as platform_repository


def save(campaign):
    sql = "INSERT INTO campaigns (name, budget_id, platform_id) VALUES (%s, %s, %s) RETURNING *"
    values = [campaign.name, campaign.budget.id, campaign.platform.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    campaign.id = id
    return campaign


def select_all():
    campaigns = []

    sql = "SELECT * FROM campaigns"
    results = run_sql(sql)

    for row in results:
        budget = budget_repository.select(row['budget_id'])
        platform = platform_repository.select(row['currency_id'])
        campaign = Campaign(row['name'], budget, platform, row['id'])
        campaigns.append(campaign)
    return campaigns


def select(id):
    campaign = None
    sql = "SELECT * FROM campaigns WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        platform = platform_repository.select(result['currency_id'])
        campaign = Campaign(result['name'], budget, platform, result['id'])
    return campaign


def delete_all():
    sql = "DELETE FROM campaigns"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM campaigns WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(campaign):
    sql = "UPDATE campaigns SET (name, budget_id, platform_id) = (%s, %s, %s) WHERE id = %s"
    values = [campaign.name, campaign.budget.id, campaign.platform, campaign.id]
    run_sql(sql, values)