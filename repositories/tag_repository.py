from db.run_sql import run_sql

from models.tag import Tag
import repositories.budget_repository as budget_repository
import repositories.account_repository as account_repository
import repositories.platform_repository as platform_repository
import repositories.campaign_repository as campaign_repository
import repositories.tag_category_repository as tag_category_repository
from collections import defaultdict


def save(tag):
    sql = "INSERT INTO tags (name, category_id, budget_id, account_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [tag.name, tag.category.id, tag.budget.id, tag.account.id]
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
        tag_category = tag_category_repository.select(row['category_id'])
        tag = Tag(row['name'], tag_category, budget, account, row['id'])
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
        tag_category = tag_category_repository.select(result['category_id'])
        tag = Tag(result['name'], tag_category, budget, account, result['id'])
    return tag


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name, category_id, budget_id, account_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [tag.name, tag.category.id, tag.budget.id, tag.account.id, tag.id]
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

    sql = "SELECT category_id, name, id FROM tags WHERE account_id = %s"
    values = [account.id]
    results = run_sql(sql, values)

    for result in results:
        tag_category = tag_category_repository.select(result['category_id'])
        tags.append({tag_category.name: {result["name"]: result["id"]}}) # type: ignore

    # Group identical category keys and their tag names
    tags_grouped = defaultdict(list)
    for dict in tags:
        for key, value in dict.items():
            tags_grouped[key].append(value)

    return tags_grouped


def get_tags_by_categories(account):
    categories = tag_category_repository.select_all_by_account(account)

    categories_with_names = []

    for category in categories:
        category_objects = []

        sql = "SELECT * FROM tags WHERE account_id = %s AND category_id = %s"
        values = [account.id, category.id] # type: ignore
        results = run_sql(sql, values)

        for row in results:
            budget = budget_repository.select(row['budget_id'])
            account = account_repository.select(row['account_id'])
            tag_category = tag_category_repository.select(row['category_id'])
            tag = Tag(row['name'], tag_category, budget, account, row['id'])
            category_objects.append(tag)
        
        category_dict = {}
        category_dict[category] = category_objects
        categories_with_names.append(category_dict)

    return categories_with_names

