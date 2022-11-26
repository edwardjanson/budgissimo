import pdb

from models.account import Account
from models.platform import Platform
from models.campaign import Campaign
from models.tag import Tag
from models.campaign_tag import CampaignTag
from models.budget import Budget
from models.currency import Currency
from models.tag_category import TagCategory

import repositories.account_repository as account_repository
import repositories.platform_repository as platform_repository
import repositories.tag_repository as tag_repository
import repositories.campaign_repository as campaign_repository
import repositories.campaign_tag_repository as campaign_tag_repository
import repositories.budget_repository as budget_repository
import repositories.currency_repository as currency_repository
import repositories.tag_category_repository as tag_category_repository


account_repository.delete_all()
platform_repository.delete_all()
tag_repository.delete_all()
campaign_repository.delete_all()
campaign_tag_repository.delete_all()
budget_repository.delete_all()
currency_repository.delete_all()


# ---------------------- Currencies ---------------------- #
british_pound = Currency("British Pound", "£")
currency_repository.save(british_pound)

euro = Currency("Euro", "€")
currency_repository.save(euro)

us_dollar = Currency("US Dollar", "$")
currency_repository.save(us_dollar)

# ---------------------- Account ---------------------- #
account_budget = Budget(10000.00, 5838.39)
budget_repository.save(account_budget)

account = Account("Client 1", account_budget, british_pound, "1WpWbclQPMMG_h2oP5CvV8TcPI2ae8-EF544yX2LmB-Q")
account_repository.save(account)

# ---------------------- Platforms ---------------------- #
# Google Ads
google_ads_budget = Budget(5000.00, 2703.53)
budget_repository.save(google_ads_budget)

google_ads = Platform("Google Ads", google_ads_budget, account)
platform_repository.save(google_ads)

# Facebook Ads
facebook_ads_budget = Budget(1500.00, 884.79)
budget_repository.save(facebook_ads_budget)

facebook_ads = Platform("Facebook Ads", facebook_ads_budget, account)
platform_repository.save(facebook_ads)

# Instagram Ads
instagram_ads_budget = Budget(1000.00, 564.03)
budget_repository.save(instagram_ads_budget)

instagram_ads = Platform("Instagram Ads", instagram_ads_budget, account)
platform_repository.save(instagram_ads)

# LinkedIn Ads
linkedin_ads_budget = Budget(2500.00, 1686.04)
budget_repository.save(linkedin_ads_budget)

linkedin_ads = Platform("LinkedIn Ads", linkedin_ads_budget, account)
platform_repository.save(linkedin_ads)

# ---------------------- Tags ---------------------- #
# --- Tag Categories --- #
promoting_category = TagCategory("Promoting", account)
tag_category_repository.save(promoting_category)

location_category = TagCategory("Location", account)
tag_category_repository.save(location_category)

type_category = TagCategory("Type", account)
tag_category_repository.save(type_category)

# --- Promoting Category --- #
# Brand Tag
brand_budget = Budget(1000.00, 709.52)
budget_repository.save(brand_budget)

brand_tag = Tag("Brand", promoting_category, brand_budget, account)
tag_repository.save(brand_tag)

# Non Brand Tag
non_brand_budget = Budget(3000.00, 1709.00)
budget_repository.save(non_brand_budget)

non_brand_tag = Tag("Non Brand", promoting_category, non_brand_budget, account)
tag_repository.save(non_brand_tag)

# Retargeting Tag
retargeting_budget = Budget(1500.00, 594.54)
budget_repository.save(retargeting_budget)

retargeting_tag = Tag("Retargeting", promoting_category, retargeting_budget, account)
tag_repository.save(retargeting_tag)

# --- Type Category --- #
# Search Tag
search_budget = Budget(4000.00, 2418.52)
budget_repository.save(search_budget)

search_tag = Tag("Search", type_category, search_budget, account)
tag_repository.save(search_tag)

# Display Tag
display_budget = Budget(1000.00, 285.01)
budget_repository.save(display_budget)

display_tag = Tag("Display", type_category, display_budget, account)
tag_repository.save(display_tag)

# Social Tag
social_budget = Budget(5000.00, 3134.86)
budget_repository.save(social_budget)

social_tag = Tag("Social", type_category, social_budget, account)
tag_repository.save(social_tag)

# --- Location Category --- #
# UK Tag
uk_budget = Budget(4750.00, 2548.52)
budget_repository.save(uk_budget)

uk_tag = Tag("UK", location_category, uk_budget, account)
tag_repository.save(uk_tag)

# Worldwide Tag
worldwide_budget = Budget(5250.00, 3289.87)
budget_repository.save(worldwide_budget)

worldwide_tag = Tag("Worldwide", location_category, worldwide_budget, account)
tag_repository.save(worldwide_tag)

# ---------------------- Campaigns ---------------------- #
# --- Google Ads Campaigns --- #
# Campaign 1
budget_1 = Budget(250.00, 209.36)
budget_repository.save(budget_1)

campaign_1 = Campaign("Brand - UK", budget_1, google_ads)
campaign_repository.save(campaign_1)

campaign_tag_1 = CampaignTag(campaign_1, brand_tag)
campaign_tag_repository.save(campaign_tag_1)

campaign_tag_20 = CampaignTag(campaign_1, search_tag)
campaign_tag_repository.save(campaign_tag_20)

campaign_tag_2 = CampaignTag(campaign_1, uk_tag)
campaign_tag_repository.save(campaign_tag_2)

# Campaign 2
budget_2 = Budget(750.00, 500.16)
budget_repository.save(budget_2)

campaign_2 = Campaign("Brand - Worldwide", budget_2, google_ads)
campaign_repository.save(campaign_2)

campaign_tag_3 = CampaignTag(campaign_2, brand_tag)
campaign_tag_repository.save(campaign_tag_3)

campaign_tag_21 = CampaignTag(campaign_2, search_tag)
campaign_tag_repository.save(campaign_tag_21)

campaign_tag_4 = CampaignTag(campaign_2, worldwide_tag)
campaign_tag_repository.save(campaign_tag_4)

# Campaign 3
budget_3 = Budget(1000.00, 463.90)
budget_repository.save(budget_3)

campaign_3 = Campaign("Non Brand - Advertising Budget Tracking - UK", budget_3, google_ads)
campaign_repository.save(campaign_3)

campaign_tag_5 = CampaignTag(campaign_3, non_brand_tag)
campaign_tag_repository.save(campaign_tag_5)

campaign_tag_23 = CampaignTag(campaign_3, search_tag)
campaign_tag_repository.save(campaign_tag_23)

campaign_tag_6 = CampaignTag(campaign_3, uk_tag)
campaign_tag_repository.save(campaign_tag_6)

# Campaign 4
budget_4 = Budget(2000.00, 1245.10)
budget_repository.save(budget_4)

campaign_4 = Campaign("Non Brand - Advertising Budget Tracking - Worldwide", budget_4, google_ads)
campaign_repository.save(campaign_4)

campaign_tag_7 = CampaignTag(campaign_4, non_brand_tag)
campaign_tag_repository.save(campaign_tag_7)

campaign_tag_24 = CampaignTag(campaign_4, search_tag)
campaign_tag_repository.save(campaign_tag_24)

campaign_tag_8 = CampaignTag(campaign_4, worldwide_tag)
campaign_tag_repository.save(campaign_tag_8)

# Campaign 5
budget_5 = Budget(1000.00, 285.01)
budget_repository.save(budget_5)

campaign_5 = Campaign("Display - Retargeting - Worldwide", budget_5, google_ads)
campaign_repository.save(campaign_5)

campaign_tag_9 = CampaignTag(campaign_5, retargeting_tag)
campaign_tag_repository.save(campaign_tag_9)

campaign_tag_25 = CampaignTag(campaign_5, display_tag)
campaign_tag_repository.save(campaign_tag_25)

campaign_tag_10 = CampaignTag(campaign_5, worldwide_tag)
campaign_tag_repository.save(campaign_tag_10)

# --- Facebook Ads Campaigns --- #
# Campaign 6
budget_6 = Budget(1000.00, 575.34)
budget_repository.save(budget_6)

campaign_6 = Campaign("Carousel - Interests In Marketing - UK", budget_6, facebook_ads)
campaign_repository.save(campaign_6)

campaign_tag_11 = CampaignTag(campaign_6, social_tag)
campaign_tag_repository.save(campaign_tag_11)

campaign_tag_12 = CampaignTag(campaign_6, uk_tag)
campaign_tag_repository.save(campaign_tag_12)

# Campaign 7
budget_7 = Budget(500.00, 309.45)
budget_repository.save(budget_7)

campaign_7 = Campaign("Carousel - Retargeting - UK", budget_7, facebook_ads)
campaign_repository.save(campaign_7)

campaign_tag_13 = CampaignTag(campaign_7, retargeting_tag)
campaign_tag_repository.save(campaign_tag_13)

campaign_tag_26 = CampaignTag(campaign_7, social_tag)
campaign_tag_repository.save(campaign_tag_26)

campaign_tag_14 = CampaignTag(campaign_7, uk_tag)
campaign_tag_repository.save(campaign_tag_14)

# --- Instagram Ads Campaigns --- #
# Campaign 8
budget_8 = Budget(1000.00, 564.03)
budget_repository.save(budget_8)

campaign_8 = Campaign("Carousel - Interests In Marketing - UK", budget_8, instagram_ads)
campaign_repository.save(campaign_8)

campaign_tag_15 = CampaignTag(campaign_8, social_tag)
campaign_tag_repository.save(campaign_tag_15)

campaign_tag_16 = CampaignTag(campaign_8, uk_tag)
campaign_tag_repository.save(campaign_tag_16)

# --- LinkedIn Ads Campaigns --- #
# Campaign 9
budget_9 = Budget(1000.00, 426.44)
budget_repository.save(budget_9)

campaign_9 = Campaign("Carousel - Working In Marketing - UK", budget_9, linkedin_ads)
campaign_repository.save(campaign_9)

campaign_tag_17 = CampaignTag(campaign_9, social_tag)
campaign_tag_repository.save(campaign_tag_17)

campaign_tag_18 = CampaignTag(campaign_9, uk_tag)
campaign_tag_repository.save(campaign_tag_18)

# Campaign 10
budget_10 = Budget(1500.00, 1259.60)
budget_repository.save(budget_10)

campaign_10 = Campaign("Carousel - Working In Marketing - Worldwide", budget_10, linkedin_ads)
campaign_repository.save(campaign_10)

campaign_tag_19 = CampaignTag(campaign_10, social_tag)
campaign_tag_repository.save(campaign_tag_19)

campaign_tag_20 = CampaignTag(campaign_10, worldwide_tag)
campaign_tag_repository.save(campaign_tag_20)


pdb.set_trace()
