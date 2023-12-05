import unittest
from calculation import Calculation


def seminar_test():
    if 8 != Calculation.calculation(2, 6, '+'):
        raise AssertionError("Ошибка в методе")

    if 0 != Calculation.calculation(2, 2, '-'):
        raise AssertionError("Ошибка в методе")

    if 14 != Calculation.calculation(2, 7, '*'):
        raise AssertionError("Ошибка в методе")

    if 2 != Calculation.calculation(100, 50, '/'):
        raise AssertionError("Ошибка в методе")

    try:
        Calculation.calculation(8, 4, '_')
    except:
        AssertionError("Ошибка в методе")

    assert 8 == Calculation.calculation(2, 6, '+')
    assert 0 == Calculation.calculation(2, 2, '-')
    assert 14 == Calculation.calculation(2, 7, '*')
    assert 2 == Calculation.calculation(100, 50, '/')


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculation()

    def test_add(self):
        self.assertEqual(self.calculator.calculation(2, 6, '+'), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.calculation(2, 2, '-'), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.calculation(2, 7, '*'), 14)

    def test_divide(self):
        self.assertEqual(self.calculator.calculation(100, 50, '/'), 2)

    def test_EqualZeroError(self):
        self.assertEqual(self.calculator.calculating_discount(100, 15), 85)

    def test_purchase_less_than_discount(self):
        self.assertEqual(self.calculator.calculating_discount(100, 101), -1)


if __name__ == "__main__":
    seminar_test()
    unittest.main()
