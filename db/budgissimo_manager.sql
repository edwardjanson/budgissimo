DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS budgets CASCADE;
DROP TABLE IF EXISTS currency CASCADE;
DROP TABLE IF EXISTS platforms CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS campaigns CASCADE;
DROP TABLE IF EXISTS campaigns_tags CASCADE;


CREATE TABLE currencies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    symbol VARCHAR(1) NOT NULL
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    monthly_budget FLOAT,
    amount_spent FLOAT
);

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    budget_id SERIAL NOT NULL REFERENCES budgets(id) ON DELETE CASCADE,
    currency_id SERIAL NOT NULL REFERENCES currencies(id)
);

CREATE TABLE platforms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    account_id SERIAL NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    budget_id SERIAL NOT NULL REFERENCES budgets(id) ON DELETE CASCADE
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    account_id SERIAL NOT NULL REFERENCES accounts(id),
    budget_id SERIAL NOT NULL REFERENCES budgets(id)
);

CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    platform_id SERIAL NOT NULL REFERENCES platforms(id),
    budget_id SERIAL NOT NULL REFERENCES budgets(id) ON DELETE CASCADE
);

CREATE TABLE campaigns_tags (
    id SERIAL PRIMARY KEY,
    campaign_id SERIAL NOT NULL REFERENCES campaigns(id),
    tag_id SERIAL NOT NULL REFERENCES tags(id)
);