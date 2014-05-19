import unittest, random, math
from search.Cities import City, Position
from search.Graph import *
from search.Search import *

class BaseGraphTestCase(unittest.TestCase):
  def setUp(self):
    nodes = {
      0: City(0, "Zion0", Position(1.5352765135104984,-25.407051236792057)),
      1: City(1, "Amsterdam1", Position(-80.89942735555584,102.4463541142299)),
      2: City(2, "Phoenix2", Position(24.713383034928697,178.20745931034742)),
      3: City(3, "State College3", Position(-78.057464912123,-120.7319949406601)),
      4: City(4, "Reno4", Position(-49.415337519725654,4.901625295542724))
      }
    graph = {0: [2], 1: [0, 2], 2: [3, 0], 3: [4], 4: [3, 2]}
    self.graph = Graph(nodes, graph)
    self.start = list(nodes)[0]
    self.finish = list(nodes)[-1]
    self.solution = [0, 2, 3, 4]

  def tearDown(self):
    self.graph = None

class SearchTestCase(BaseGraphTestCase):
  def testBackTrack(self):
    obj = Backtrack(self.graph.nodes, self.graph.graph)
    path = obj.search(self.start, self.finish)
    print(path)
    assert(self.solution == path)

  def testDijkstra(self):
    obj = Dijkstra(self.graph.nodes, self.graph.graph)
    verticies = list(obj.nodes)
    distances, path = obj.search(verticies[0], verticies[-1])
    print(path)
    assert(self.solution == path)

## test configuration
#######################

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SearchTestCase)
    return suite

if __name__ == "__main__":
  #unittest.main()
  runner = unittest.TextTestRunner()
  test_suite = suite()
  runner.run(test_suite)
