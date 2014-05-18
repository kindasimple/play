import unittest, random
from maths import Number, Arithmetic
from sort import Sorting

class BaseSortTestCase(unittest.TestCase):
  def setUp(self):
    self.math = Arithmetic()
    self.sort = Sorting()
    self.sorted = self.generateSortedList(10)
    self.shuffled = self.generateShuffledList(10)

  def tearDown(self):
    self.sort = None
    self.math = None
    self.sorted = None
    self.shuffled = None

  def generateSortedList(self, length):
    items = list(range(1, 1 + length + 1))
    numbers = []
    for item in items:
      numbers.append(Number(item))
    return numbers

  def generateShuffledList(self, length):
    items = list(range(1, 1 + length + 1))
    random.shuffle(items)
    numbers = []
    for item in items:
      numbers.append(Number(item))
    return numbers

  def checkSortedList(self, original, sorted):
    for idx, item in enumerate(sorted):
      if not self.math.Equals(item, original[idx]):
        return False
    return True

class SortingTestCase(BaseSortTestCase):
  def testQuicksort(self):
    sorted = self.sort.Quicksort(self.shuffled)
    self.assertTrue(self.checkSortedList(self.sorted, sorted), 'incorrect result')

  def testMergesort(self):
    sorted = self.sort.Mergesort(self.shuffled)
    self.assertTrue(self.checkSortedList(self.sorted, sorted), 'incorrect result')


  def testHeapsortSiftDown(self):
    sorted = self.sort.HeapsortSiftDown(list(self.shuffled))
    self.assertTrue(self.checkSortedList(self.sorted, sorted), 'incorrect result')

  def testHeapsortSiftUp(self):
    sorted = self.sort.HeapsortSiftUp(list(self.shuffled))
    self.assertTrue(self.checkSortedList(self.sorted, sorted), 'incorrect result')

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
