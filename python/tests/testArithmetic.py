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

class ArithmeticTestSuite(unittest.TestSuite):
	def __init__(self):
		unittest.TestSuite.__init__(self, map(ArithmeticTestCase, ("testAdd","testSubtract")))

if __name__ == "__main__":
	unittest.main()
