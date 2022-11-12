import unittest
from models.tag import Tag
from models.budget import Budget
from models.account import Account
from models.currency import Currency


class TestTag(unittest.TestCase):
    
    def setUp(self):
        self.currency_1 = Currency("British Pounds", "£", "left")
        self.budget_1 = Budget(500.00, 30.00)
        self.account_1 = Account(self.budget_1, self.currency_1)
        self.tag_1 = Tag("Test tag", self.budget_1, self.account_1)
    
    def test_tag_has_name(self):
        self.assertEqual("Test tag", self.tag_1.name)
    
    def test_tag_has_a_budget(self):
        self.assertEqual(500.00, self.tag_1.budget.monthly_budget)

    def test_tag_has_an_account(self):
        self.assertEqual(500.00, self.tag_1.account.budget.monthly_budget)

    def test_updating_the_tag_name(self):
        self.tag_1.update_name("New test")
        self.assertEqual("New test", self.tag_1.name)
    
    def test_updating_the_tag_budget(self):
        budget_2 = Budget(525.00, 30.00)
        self.tag_1.update_budget(budget_2)
        self.assertEqual(525.00, self.tag_1.budget.monthly_budget)