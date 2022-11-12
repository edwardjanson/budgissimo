from db.run_sql import run_sql

from models.tag import Tag
import repositories.budget_repository as budget_repository
import repositories.account_repository as account_repository
import repositories.campaign_repository as campaign_repository


def save(tag):
    sql = "INSERT INTO tags (name, budget_id, account_id) VALUES (%s, %s, %s) RETURNING *"
    values = [tag.name, tag.budget.id, tag.account]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag


def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        budget = budget_repository.select(row['budget_id'])
        account = account_repository.select(row['currency_id'])
        tag = Tag(row['name'], budget, account, row['id'])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        account = account_repository.select(result['currency_id'])
        tag = Tag(result['name'], budget, account, result['id'])
    return tag


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name, budget_id, account_id) = (%s, %s, %s) WHERE id = %s"
    values = [tag.name, tag.budget.id, tag.account, tag.id]
    run_sql(sql, values)


def campaigns(tag):
    campaigns = []

    sql = "SELECT campaign_id FROM campaign_tag WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for result in results:
        campaign = campaign_repository.select(result["campaign_id"])
        campaigns.append(campaign)
    
    return campaigns