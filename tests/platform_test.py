import unittest
from models.platform import Platform
from models.budget import Budget
from models.account import Account
from models.currency import Currency


class TestPlatform(unittest.TestCase):
    
    def setUp(self):
        self.currency_1 = Currency("British Pounds", "£", "left")
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.account_1 = Account(self.budget_1, self.currency_1)
        self.platform_1 = Platform("Test platform", self.budget_1, self.account_1)
    
    def test_platform_has_name(self):
        self.assertEqual("Test platform", self.platform_1.name)
    
    def test_platform_has_a_budget(self):
        self.assertEqual(500.00, self.platform_1.budget.monthly_budget)

    def test_platform_has_an_account(self):
        self.assertEqual(500.00, self.platform_1.account.budget.monthly_budget)

    def test_updating_the_platform_name(self):
        self.platform_1.update_name("New test")
        self.assertEqual("New test", self.platform_1.name)
    
    def test_updating_the_platform_budget(self):
        budget_2 = Budget(525.00, 17.00, 30.00)
        self.platform_1.update_budget(budget_2)
        self.assertEqual(525.00, self.platform_1.budget.monthly_budget)