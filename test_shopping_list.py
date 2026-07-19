import unittest
from shopping_list import ShoppingList
class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list =shopping_list = ShoppingList({"napkin":8,"hat":30,"shoes":15})
    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(),3)
    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(),53)
