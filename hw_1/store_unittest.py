import unittest

from produce import Produce
from store import Store


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Produce('apple', 5)
        self.b = Produce('strawberry', 15)
        self.c = Produce('banana', 10)
        self.d = Produce('watermelon', 8)
        self.e = Produce('pear', 6)
        self.product_list = [self.a, self.b, self.c, self.d, self.e]
        self.shop = Store(self.product_list)

    def test_get_products(self):
        for product in self.product_list:
            self.assertIsInstance(product, Produce)

    def test_set_products(self):
        self.failureException(self.shop.set_products(self.product_list), self.shop)

    def test_sorted_list_products(self):
        shop = self.shop.get_sorted_list_products()
        for i in range(len(shop) - 1):
            tmp = shop[i].cost
            self.assertGreaterEqual(shop[i + 1].cost, tmp)

    def test_most_expensive_product(self):
        self.assertEqual(self.shop.get_most_expensive_product().cost,
                         max(self.product_list, key=lambda x: x.cost).cost)


if __name__ == "__main__":
    unittest.main()
