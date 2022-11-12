from db.run_sql import run_sql

from models.campaign_tag import CampaignTag
import repositories.campaign_repository as campaign_repository
import repositories.tag_repository as tag_repository


def save(account):
    sql = "INSERT INTO accounts (campaign_id, tag_id) VALUES (%s, %s) RETURNING *"
    values = [account.campaign.id, account.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id
    return account


def select_all():
    accounts = []

    sql = "SELECT * FROM accounts"
    results = run_sql(sql)

    for row in results:
        campaign = campaign_repository.select(row['campaign_id'])
        tag = tag_repository.select(row['tag_id'])
        account = CampaignTag(campaign, tag, row['id'])
        accounts.append(account)
    return accounts


def select(id):
    account = None
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        campaign = campaign_repository.select(result['campaign_id'])
        tag = tag_repository.select(result['tag_id'])
        account = CampaignTag(campaign, tag, result['id'])
    return account


def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM accounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(account):
    sql = "UPDATE accounts SET (campaign_id, tag_id) = (%s, %s) WHERE id = %s"
    values = [account.campaign.id, account.tag.id, account.id]
    run_sql(sql, values)