from db.run_sql import run_sql

from models.currency import Currency


def save(currency):
    sql = "INSERT INTO currencies (name, symbol, symbol_location) VALUES (%s, %s, %s) RETURNING *"
    values = [currency.name, currency.symbol, currency.symbol_location]
    results = run_sql(sql, values)
    id = results[0]['id']
    currency.id = id
    return currency


def select_all():
    currencies = []

    sql = "SELECT * FROM currencies"
    results = run_sql(sql)

    for row in results:
        currency = Currency(row['name'], row['symbol'], row['symbol_location'], row['id'])
        currencies.append(currency)
    return currencies


def select(id):
    currency = None
    sql = "SELECT * FROM currencies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        currency = Currency(result['name'], result['symbol'], result['symbol_location'], result['id'])
    return currency


def delete_all():
    sql = "DELETE FROM currencies"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM currencies WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(currency):
    sql = "UPDATE currencies SET (name, symbol, symbol_location) = (%s, %s, %s) WHERE id = %s"
    values = [currency.name, currency.symbol, currency.symbol_location]
    run_sql(sql, values)