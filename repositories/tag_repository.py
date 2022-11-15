from db.run_sql import run_sql

from models.tag import Tag
import repositories.budget_repository as budget_repository
import repositories.account_repository as account_repository
import repositories.campaign_repository as campaign_repository
from collections import defaultdict


def save(tag):
    sql = "INSERT INTO tags (name, category, budget_id, account_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [tag.name, tag.category, tag.budget.id, tag.account.id]
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
        account = account_repository.select(row['account_id'])
        tag = Tag(row['name'], row['category'], budget, account, row['id'])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        account = account_repository.select(result['account_id'])
        tag = Tag(result['name'], result['category'], budget, account, result['id'])
    return tag


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name, category, budget_id, account_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [tag.name, tag.category, tag.budget.id, tag.account.id, tag.id]
    run_sql(sql, values)


def select_all_by_account(account):
    tags = []

    sql = "SELECT id FROM tags WHERE account_id = %s"
    values = [account.id]
    results = run_sql(sql, values)

    for result in results:
        tag = select(result["id"])
        tags.append(tag)
    
    return tags


def get_tag_categories_and_names(account):
    tags = []

    sql = "SELECT category, name, id FROM tags WHERE account_id = %s"
    values = [account.id]
    results = run_sql(sql, values)

    for result in results:
        tags.append({result["category"]: {result["name"]: result["id"]}})

    # Group identical category keys and their tag names
    tags_grouped = defaultdict(list)
    for dict in tags:
        for key, value in dict.items():
            tags_grouped[key].append(value)

    return tags_grouped