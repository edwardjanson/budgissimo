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




pdb.set_trace()
