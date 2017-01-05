import unittest
from format_price import format_price

class FormatPriceTest(unittest.TestCase):
    def test_string_value(self):
        self.assertEqual('1', format_price('1'))
        self.assertEqual('3 240', format_price('3240.0'))

    def test_many_zeros(self):
        self.assertEqual('1', format_price(1.0000))

    def test_int_value(self):
        self.assertEqual('1', format_price(1))

    def test_float_with_frac(self):
        self.assertEqual('1.02', format_price(1.0212))

    def test_none_value(self):
        with self.assertRaises(ValueError):
            format_price(None)

    def test_dummy_value(self):
        with self.assertRaises(ValueError):
            format_price('spam')

    def test_spaces(self):
        self.assertEqual('3 245', format_price(3245))

if __name__ == '__main__':
    unittest.main()
        