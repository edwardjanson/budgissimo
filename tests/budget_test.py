import unittest
from models.budget import Budget


class TestBudget(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 17.00, 30.00)
    
    def budget_has_a_monthly_budget(self):
        self.assertEqual(500.00, self.budget_1.monthly_budget)
    
    def budget_has_a_daily_budget(self):
        self.assertEqual(17.00, self.budget_1.daily_budget)

    def budget_has_an_amount_spent(self):
        self.assertEqual(30.00, self.budget_1.amount_spent)
    
    def test_updating_monthly_budget(self):
        self.budget_1.update_monthly_budget(525.00)
        self.assertEqual(525.00, self.budget_1.monthly_budget)

    def test_updating_daily_budget(self):
        self.budget_1.update_daily_budget(40.00)
        self.assertEqual(40.00, self.budget_1.daily_budget)

    def test_updating_amount_spent(self):
        self.budget_1.update_amount_spent(50.00)
        self.assertEqual(50.00, self.budget_1.amount_spent)