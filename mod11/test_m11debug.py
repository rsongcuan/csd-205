import unittest
from m11debug import investment_function

class InvestmentTestCase(unittest.TestCase):
	def test_investment(self):
		years_to_double = investment_function()
		self.assertEqual(years_to_double, 8)

if __name__ == '__main__':
	unittest.main()