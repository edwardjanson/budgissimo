import unittest
from models.platform import Platform
from models.budget import Budget


class TestPlatform(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.platform_1 = Platform("Test platform", self.budget_1)
    
    def test_campaign_has_name(self):
        self.assertEqual("Test platform", self.platform_1.name)
    
    def test_campaign_has_a_budget(self):
        self.assertEqual(500.00, self.platform_1.budget.monthly_budget)

    def test_updating_the_name(self):
        self.platform_1.update_name("New test")
        self.assertEqual("New test", self.platform_1.name)
    
    def test_updating_the_budget(self):
        budget_2 = Budget(525.00, 17.00, 30.00)
        self.platform_1.update_budget(budget_2)
        self.assertEqual(525.00, self.platform_1.budget.monthly_budget)