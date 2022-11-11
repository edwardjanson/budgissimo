import unittest
from models.account import Account
from models.budget import Budget
from models.currency import Currency


class TestAccount(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.currency_1 = Currency("British Pounds", "£", "left")
        self.account_1 = Account(self.budget_1, self.currency_1)
    
    def test_account_has_a_budget(self):
        self.assertEqual(500.00, self.account_1.budget.monthly_budget)
    
    def test_updating_the_budget(self):
        budget_2 = Budget(525.00, 17.00, 30.00)
        self.account_1.update_budget(budget_2)
        self.assertEqual(525.00, self.account_1.budget.monthly_budget)

    def test_updating_the_currency(self):
        currency_2 = Currency("Euros", "€", "right")
        self.account_1.update_currency(currency_2)
        self.assertEqual("Euros", self.account_1.currency.name)