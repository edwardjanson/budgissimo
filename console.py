import pdb

from models.account import Account
from models.platform import Platform
from models.campaign import Campaign
from models.tag import Tag
from models.campaign_tag import CampaignTag
from models.budget import Budget
from models.currency import Currency

import repositories.account_repository as account_repository
import repositories.platform_repository as platform_repository
import repositories.tag_repository as tag_repository
import repositories.campaign_repository as campaign_repository
import repositories.campaign_tag_repository as campaign_tag_repository
import repositories.budget_repository as budget_repository
import repositories.currency_repository as currency_repository


account_repository.delete_all()
platform_repository.delete_all()
tag_repository.delete_all()
campaign_repository.delete_all()
campaign_tag_repository.delete_all()
budget_repository.delete_all()
currency_repository.delete_all()


# Currencies
british_pound = Currency("British Pound", "£")
euro = Currency("Euro", "€")
us_dollar = Currency("US Dollar", "$")

# Account
account_budget = Budget(10000.00, 322.00)
account = Account(account_budget, british_pound)

# Platforms
google_ads_budget = Budget(5000.00, 15.00)
google_ads = Platform("Google Ads", google_ads_budget, account)

facebook_ads_budget = Budget(2000.00, 64.00)
facebook_ads = Platform("Facebook Ads", facebook_ads_budget, account)

instagram_ads_budget = Budget(2500.00, 80.00)
instagram_ads = Platform("Instagram Ads", instagram_ads_budget, account)

linkedin_ads_budget = Budget(1500.00, 48.00)
linkedin_ads = Platform("LinkedIn Ads", linkedin_ads_budget, account)



pdb.set_trace()
