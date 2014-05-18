import unittest
from maths import Number, Arithmetic

class BaseArithmeticTestCase(unittest.TestCase):
	def setUp(self):
		self.math = Arithmetic()

	def tearDown(self):
		self.math = None

class ArithmeticTestCase(BaseArithmeticTestCase):
	def testAdd(self):
		addend1 = Number(5)
		addend2 = Number(2)
		sum = Number(7)

		self.assertTrue(self.math.Equals(self.math.Add(addend1, addend2), sum), 'incorrect result')

	def testSubtract(self):
		minuend = Number(5)
		subtrahend = Number(2)
		difference = Number(3)

		self.assertTrue(self.math.Equals(self.math.Subtract(minuend, subtrahend), difference), 'incorrect result')

	def testMultiply(self):
		multiplicand = Number(2)
		multiplier = Number(4)
		product = Number(2*4)

		self.assertTrue(self.math.Equals(self.math.Multiply(multiplicand, multiplier), product), 'incorrect result')

	def testDivide(self):
		dividend = Number(8)
		divisor = Number(4)
		quotient = Number(8/4)

		self.assertTrue(self.math.Equals(self.math.Divide(dividend, divisor), quotient), 'incorrect result')

	def testLessThan(self):
		first = Number(1)
		second = Number(2)
		lessThanResult = 1 < 2
		greaterThanResult = 1 > 2

		self.assertTrue(self.math.LessThan(first, second) == lessThanResult, 'incorrect result')
		self.assertTrue(self.math.GreaterThan(first, second) == greaterThanResult, 'incorrect result')

## test configuration
#######################

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ArithmeticTestCase)
    return suite

if __name__ == "__main__":
	#unittest.main()
	runner = unittest.TextTestRunner()
	test_suite = suite()
	runner.run(test_suite)
