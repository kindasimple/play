import unittest
from maths import Number, Arithmetic
from sort import Quicksort

class BaseSortTestCase(unittest.TestCase):
  def setUp(self):
    self.math = Arithmetic()
    self.qs = Quicksort()

  def tearDown(self):
    self.qs = None
    self.math = None

class QuicksortTestCase(BaseSortTestCase):
  def testQuicksort(self):
    unsorted = [Number(2), Number(1), Number(5)]
    sorted = self.qs.Sort(unsorted)

    self.assertTrue(self.math.Equals(Number(1), sorted[0]), 'incorrect result')
    self.assertTrue(self.math.Equals(Number(2), sorted[1]), 'incorrect result')
    self.assertTrue(self.math.Equals(Number(5), sorted[2]), 'incorrect result')

## test configuration
#######################

def suite():
    suite = unittest.TestSuite()
    suite.addTest(QuicksortTestCase)
    return suite

if __name__ == "__main__":
  #unittest.main()
  runner = unittest.TextTestRunner()
  test_suite = suite()
  runner.run(test_suite)
