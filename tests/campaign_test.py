import unittest
from models.campaign import Campaign
from models.budget import Budget


class TestCampaign(unittest.TestCase):
    
    def setUp(self):
        budget_1 = Budget(500.00, 17.00, 30.00)
        budget_2 = Budget(5000.00, 170.00, 300.00)
        self.campaign_1 = Campaign("Test campaign", budget_1)
    
    def campaign_has_name(self):
        self.assertEqual("Test campaign", self.campaign_1.name)
    
    def campaign_has_a_budget(self):
        self.assertEqual(500.00, self.campaign_1.budget.monthly_budget)
    
    def test_updating_the_budget(self):
        budget_2 = Budget(525.00, 17.00, 30.00)
        self.campaign_1.update_budget(budget_2)
        self.assertEqual(525.00, self.campaign_1.budget.monthly_budget)