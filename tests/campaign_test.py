import unittest
from models.campaign import Campaign
from models.budget import Budget
from models.platform import Platform
from models.account import Account
from models.currency import Currency


class TestCampaign(unittest.TestCase):
    
    def setUp(self):
        self.currency_1 = Currency("British Pounds", "£", "left")
        self.budget_1 = Budget(500.00, 30.00)
        self.account_1 = Account(self.budget_1, self.currency_1)
        self.platform_1 = Platform("Google Ads", self.budget_1, self.account_1)
        self.campaign_1 = Campaign("Test campaign", self.budget_1, self.platform_1)
    
    def test_campaign_has_name(self):
        self.assertEqual("Test campaign", self.campaign_1.name)
    
    def test_campaign_has_a_budget(self):
        self.assertEqual(500.00, self.campaign_1.budget.monthly_budget)

    def test_campaign_has_a_platform(self):
        self.assertEqual("Google Ads", self.campaign_1.platform.name)

    def test_updating_the_campaign_name(self):
        self.campaign_1.update_name("New test")
        self.assertEqual("New test", self.campaign_1.name)
    
    def test_updating_the_campaign_budget(self):
        budget_2 = Budget(525.00, 30.00)
        self.campaign_1.update_budget(budget_2)
        self.assertEqual(525.00, self.campaign_1.budget.monthly_budget)