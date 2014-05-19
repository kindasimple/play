import math, random
from search.Cities import *

class Graph:
  def __init__(self, nodes = None, graph = None):
    if nodes:
      self.nodes = nodes
    else:
      self.nodes = self._generate_random_nodes()

    if graph:
      self.graph = graph
    else:
      self.graph = self._generate_random_graph()

  def generate_graph(self, size, connectivity):
    self.nodes = self._generate_random_nodes(size)
    self.graph = self._generate_random_graph(connectivity)

  def _generate_random_nodes(self, size = 5):
    size = math.floor(size)
    id = 0
    cities = {}
    city_names = [
        "Austin", "Detroit", "State College", "Reno", "Waco", "Springfield", "Zion",
        "Phoenix", "Amsterdam", "Elmira", "Memphis"]
    city_name_count = len(city_names)
    while id < size:
      remaining = size - id
      take = 0
      if remaining > city_name_count:
        take = city_name_count
      else:
        take = remaining
      #print("id: {}, size: {}, {}".format(id, size, take))
      for name in random.sample(city_names, take):
        cities[id+1] = City(id+1, name, self._get_random_position())
        id += 1
    return cities

  def _generate_random_graph(self, connectivity = .5):
    graph = {}
    for node in self.nodes:
      edges = random.sample(
        list(self.nodes),
        math.floor(connectivity*len(list(self.nodes)))
        )
      if node in edges: edges.remove(node)
      graph[node] = edges
    return graph

  def _get_random_position(self) :
    lat = random.randrange(-90, 90, 1) + random.random()
    lon = random.randrange(-180, 180, 1) + random.random()
    return Position(lat, lon)
