DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaigns_tags;


CREATE accounts (
  id SERIAL PRIMARY KEY
)

CREATE platforms (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  monthly_budget FLOAT,
  daily_budget FLOAT,
  account_id SERIAL NOT NULL REFERENCES accounts(id)
)

CREATE tags (
  id SERIAL PRIMARY KEY,
  monthly_budget FLOAT,
  daily_budget FLOAT,
  name VARCHAR(255)
)

CREATE campaigns (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  monthly_budget FLOAT,
  daily_budget FLOAT,
  amount_spent FLOAT,
  platform_id SERIAL NOT NULL REFERENCES platforms(id)
)

CREATE campaigns_tags (
  id SERIAL PRIMARY KEY,
  campaign_id SERIAL NOT NULL REFERENCES platforms(id),
  tags_id SERIAL NOT NULL REFERENCES tags(id)
)