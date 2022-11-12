import unittest
from models.currency import Currency


class TestCurrency(unittest.TestCase):
    
    def setUp(self):
        self.currency_1 = Currency("British Pounds", "£", "left")
    
    def test_currency_has_name(self):
        self.assertEqual("British Pounds", self.currency_1.name)

    def test_currency_has_symbol(self):
        self.assertEqual("£", self.currency_1.symbol)

    def currency_has_symbol_location(self):
        self.assertEqual("left", self.currency_1.symbol_location)