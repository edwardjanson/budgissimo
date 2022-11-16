import unittest
from models.tag_category import TagCategory


class TestTagCategory(unittest.TestCase):
    
    def setUp(self):
        self.tag_category_1 = TagCategory("Location")
    
    def test_tag_category_has_name(self):
        self.assertEqual("Location", self.tag_category_1.name)