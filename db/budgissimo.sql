DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS budgets;
DROP TABLE IF EXISTS currency;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaigns_tags;


CREATE accounts (
    id SERIAL PRIMARY KEY,
    budget_id SERIAL NOT NULL REFERENCES budget(id),
    currency_id SERIAL NOT NULL REFERENCES currency(id)
)

CREATE budgets (
    id SERIAL PRIMARY KEY,
    monthly_budget FLOAT,
    daily_budget FLOAT,
    amount_spent FLOAT
)

CREATE currency (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(1) NOT NULL
)

CREATE platforms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    account_id SERIAL NOT NULL REFERENCES accounts(id),
    budget_id SERIAL NOT NULL REFERENCES budgets(id)
)

CREATE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    account_id SERIAL NOT NULL REFERENCES accounts(id),
    budget_id SERIAL NOT NULL REFERENCES budgets(id)
)

CREATE campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    platform_id SERIAL NOT NULL REFERENCES platforms(id),
    budget_id SERIAL NOT NULL REFERENCES budgets(id)
)

CREATE campaigns_tags (
    id SERIAL PRIMARY KEY,
    campaign_id SERIAL NOT NULL REFERENCES platforms(id),
    tags_id SERIAL NOT NULL REFERENCES tags(id)
)