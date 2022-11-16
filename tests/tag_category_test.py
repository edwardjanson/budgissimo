import unittest
from models.tag_category import TagCategory
from models.budget import Budget
from models.currency import Currency
from models.account import Account


class TestTagCategory(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 30.00)
        self.currency_1 = Currency("British Pounds", "£")
        self.account_1 = Account(self.budget_1, self.currency_1)
        self.tag_category_1 = TagCategory("Location", self.account_1)
    
    def test_tag_category_has_name(self):
        self.assertEqual("Location", self.tag_category_1.name)
    
    def test_tag_has_an_account(self):
        self.assertEqual(500.00, self.tag_category_1.account.budget.monthly_budget)