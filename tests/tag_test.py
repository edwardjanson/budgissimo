import unittest
from models.tag import Tag
from models.budget import Budget


class TestTag(unittest.TestCase):
    
    def setUp(self):
        self.budget_1 = Budget(500.00, 17.00, 30.00)
        self.tag_1 = Tag("Test tag", self.budget_1)
    
    def campaign_has_name(self):
        self.assertEqual("Test tag", self.tag_1.name)
    
    def campaign_has_a_budget(self):
        self.assertEqual(500.00, self.tag_1.budget.monthly_budget)

    def test_updating_the_name(self):
        self.tag_1.update_name("New test")
        self.assertEqual("New test", self.tag_1.name)
    
    def test_updating_the_budget(self):
        budget_2 = Budget(525.00, 17.00, 30.00)
        self.tag_1.update_budget(budget_2)
        self.assertEqual(525.00, self.tag_1.budget.monthly_budget)