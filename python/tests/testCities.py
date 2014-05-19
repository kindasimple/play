import unittest, random, math
from search.Cities import City, Position

class InitTestCase(unittest.TestCase):
  def testPosition(self):
    position = Position(44.2, 102.2222)
    self.assertTrue(position)

  def testCity(self):
    position = Position(44.2, 102.2222)
    city = City(1, "Austin", position)
    self.assertTrue(city)


class BaseCityTestCase(unittest.TestCase):
  def setUp(self):
    self.sampleNames = ["Austin", "Detroit", "State College", "Reno"]
    self.cities = []
    for idx, name in enumerate(random.sample(self.sampleNames, 3)) :
      self.cities.append(City(idx, name, self.getRandomPosition()))

  def tearDown(self):
    self.sampleNames = None
    self.cities = None

  def getRandomPosition(self) :
    return Position(random.randrange(-90, 90, 1) + random.random(),  random.randrange(-180, 180, 1) + random.random())

class CreateCityTestCase(BaseCityTestCase) :
  def testDistances(self) :
    print(self.cities)
    distances = []
    for initial in self.cities :
      row = []
      for final in self.cities :
        row.append(initial.get_distance(final))
      distances.append(row)
    print(distances)
    for i, cities in enumerate(distances):
      for j, d in enumerate(cities):
        if(i == j):
          self.assertTrue(d == 0)
        else:
          self.assertTrue(d > 0)

## test configuration
#######################

def suite():
    suite = unittest.TestSuite()
    suite.addTest(InitTestCase)
    suite.addTest(CreateCityTestCase)
    return suite

if __name__ == "__main__":
  #unittest.main()
  runner = unittest.TextTestRunner()
  test_suite = suite()
  runner.run(test_suite)
