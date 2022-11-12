from db.run_sql import run_sql

from models.platform import Platform
import repositories.budget_repository as budget_repository
import repositories.account_repository as account_repository


def save(platform):
    sql = "INSERT INTO platforms (name, budget_id, account_id) VALUES (%s, %s, %s) RETURNING *"
    values = [platform.name, platform.budget.id, platform.account.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    platform.id = id
    return platform


def select_all():
    platforms = []

    sql = "SELECT * FROM platforms"
    results = run_sql(sql)

    for row in results:
        budget = budget_repository.select(row['budget_id'])
        account = account_repository.select(row['currency_id'])
        platform = Platform(row['name'], budget, account, row['id'])
        platforms.append(platform)
    return platforms


def select(id):
    platform = None
    sql = "SELECT * FROM platforms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        account = account_repository.select(result['currency_id'])
        platform = Platform(result['name'], budget, account, result['id'])
    return platform


def delete_all():
    sql = "DELETE FROM platforms"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM platforms WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(platform):
    sql = "UPDATE platforms SET (name, budget_id, account_id) = (%s, %s, %s) WHERE id = %s"
    values = [platform.name, platform.budget.id, platform.account, platform.id]
    run_sql(sql, values)