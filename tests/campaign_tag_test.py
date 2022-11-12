import unittest
from models.tag import Tag
from models.campaign_tag import CampaignTag
from models.campaign import Campaign
from models.budget import Budget
from models.platform import Platform
from models.account import Account
from models.currency import Currency


class TestCampaignTag(unittest.TestCase):
    
    def setUp(self):
        self.currency_1 = Currency("British Pounds", "£", "left")
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.budget_2 = Budget(400.00, 10.00, 20.00)
        self.account_1 = Account(self.budget_1, self.currency_1)
        self.platform_1 = Platform("Google Ads", self.budget_1, self.account_1)
        self.tag_1 = Tag("Test tag", self.budget_1, self.platform_1)
        self.campaign_1 = Campaign("Test campaign", self.budget_2, self.platform_1)
        self.campaign_tag_1 = CampaignTag(self.campaign_1, self.tag_1)
    
    def test_campaign_tag_has_tag(self):
        self.assertEqual("Test tag", self.campaign_tag_1.tag.name)

    def test_campaign_tag_has_campaign(self):
        self.assertEqual("Test campaign", self.campaign_tag_1.campaign.name)