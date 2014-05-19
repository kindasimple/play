from search.Cities import *
from search.Graph import *
from search.Error import *

class Backtrack(Graph):
  def search(self, start, finish):
    return self._find_path(start, finish)

  def _find_path(self, start, end, path=[]):
    """Source: https://www.python.org/doc/essays/graphs/"""
    path = path + [start]
    if start == end:
      return path
    if not start in self.graph:
      return None
    for node in self.graph[start]:
      if node not in path:
        newpath = self._find_path(node, end, path)
        if newpath: return newpath
    return None

class Dijkstra(Graph):
  """Pseudocode: http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"""
  def get_subdict(self, d, keys, default=None):
    return dict([ (k, d.get(k, default)) for k in keys ])

  def search(self, start, finish):
    path_length = 0

    unvisited = list(self.nodes)

    distances = {}
    previous = {}
    for node in self.nodes:
      distances[node] = float('inf')
      previous[node] = None

    distances[start] = 0

    while unvisited:
      available = self.get_subdict(distances, unvisited)
      current = min(available, key=available.get)
      #print("Working on {}".format(current))
      unvisited.remove(current)

      if distances[current] == float('inf'):
        raise SearchError("There is no path to the goal in the graph")

      if current is finish:
        break

      unvisited_neighbors = set(self.graph[current]).intersection(unvisited)
      for neighbor in unvisited_neighbors:
        distance = self.nodes[current].get_distance(self.nodes[neighbor])
        #print("Distance between {} and {} is {}".format(current, neighbor, distance))
        if distances[neighbor] > distances[current] + distance:
          distances[neighbor] = distance
          previous[neighbor] = current


    path = [current]
    while previous[current]:
      path.insert(0,previous[current])
      current = previous[current]
    path.insert(0, previous[current])
    #print(previous)
    return distances, path
