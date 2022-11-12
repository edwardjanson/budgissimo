from db.run_sql import run_sql

from models.budget import Budget


def save(budget):
    sql = "INSERT INTO budgets (monthly_budget, daily_budget, amount_spent) VALUES (%s, %s, %s) RETURNING *"
    values = [budget.monthly_budget, budget.daily_budget, budget.amount_spent]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id
    return budget


def select_all():
    budgets = []

    sql = "SELECT * FROM budgets"
    results = run_sql(sql)

    for row in results:
        budget = Budget(row['monthly_budget'], row['daily_budget'], row['amount_spent'], row['id'])
        budgets.append(budget)
    return budgets


def select(id):
    budget = None
    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = Budget(result['monthly_budget'], result['daily_budget'], result['amount_spent'], result['id'])
    return budget


def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM budgets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(budget):
    sql = "UPDATE budgets SET (monthly_budget, daily_budget, amount_spent) = (%s, %s, %s) WHERE id = %s"
    values = [budget.monthly_budget, budget.daily_budget, budget.amount_spent, budget.id]
    run_sql(sql, values)