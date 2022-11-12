from db.run_sql import run_sql

from models.account import Account
import repositories.budget_repository as budget_repository


def save(account):
    sql = "INSERT INTO accounts (budget_id, currency_id) VALUES (%s, %s) RETURNING *"
    values = [account.budget.id, account.currency.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id
    return account


def select_all():
    accounts = []

    sql = "SELECT * FROM accounts"
    results = run_sql(sql)

    for row in results:
        budget = budget_repository.select(row['budget_id'])
        currency = budget_repository.select(row['currency_id'])
        account = Account(budget, currency, row['id'])
        accounts.append(account)
    return accounts


def select(id):
    account = None
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = budget_repository.select(result['budget_id'])
        currency = budget_repository.select(result['currency_id'])
        account = Account(budget, currency, result['id'])
    return account


def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM accounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(account):
    sql = "UPDATE accounts SET (budget_id, currency_id) = (%s, %s) WHERE id = %s"
    values = [account.budget.id, account.currency.id, account.id]
    run_sql(sql, values)