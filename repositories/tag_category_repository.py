from db.run_sql import run_sql

from models.tag_category import TagCategory


def save(tag_category):
    sql = "INSERT INTO tag_categories (name, account_id) VALUES (%s, %s) RETURNING *"
    values = [tag_category.name, tag_category.account.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag_category.id = id
    return tag_category


def select_all():
    tag_categories = []

    sql = "SELECT * FROM tag_categories"
    results = run_sql(sql)

    for row in results:
        tag_category = TagCategory(row['name'], row['account_id'], row['id'])
        tag_categories.append(tag_category)
    return tag_categories


def select(id):
    tag_category = None
    sql = "SELECT * FROM tag_categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag_category = TagCategory(result['name'], result['account_id'], result['id'])
    return tag_category


def delete_all():
    sql = "DELETE FROM tag_categories"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tag_categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag_category):
    sql = "UPDATE tag_categories SET (name, account_id) = (%s, %s) WHERE id = %s"
    values = [tag_category.name, tag_category.account.id, tag_category.id]
    run_sql(sql, values)


def select_all_by_account(account):
    tag_categories = []

    sql = "SELECT id FROM tag_categories WHERE account_id = %s"
    values = [account.id]
    results = run_sql(sql, values)

    for result in results:
        tag_category = select(result["id"])
        tag_categories.append(tag_category)
    
    return tag_categories