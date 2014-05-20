from search.Cities import *
from search.Graph import *
from search.Error import *

class AStar(Graph):
  """Pseudocode from: http://en.wikipedia.org/wiki/A*_search_algorithm"""
  def search(self, start, finish):
    closed = []
    open_ = [start]
    previous = {}

    g_score = { start: 0 }
    f_score = { start: g_score[start] }

    while open_:
      available = Util.get_subdict(f_score, open_)
      current = min(available, key=available.get)
      if current == finish:
        return self.get_history(previous, finish)

      open_.remove(current)
      closed.append(current)
      for neighbor in self.graph[current]:
        if neighbor in closed:
          continue

        distance = self.nodes[current].get_distance(self.nodes[neighbor])
        node_g_score = g_score[current] +  distance

        if neighbor not in open_ or node_g_score < g_score[neighbor]:
          previous[neighbor] = current
          g_score[neighbor] = node_g_score
          f_score[neighbor] = g_score[neighbor] + self.heuristic_cost_estimate(start, finish, neighbor)
          if neighbor not in open_:
              open_.append(neighbor)

  def get_history(self, previous, current):
    if current in previous:
      path = self.get_history(previous, previous[current])
      return path + [current]
    else:
      return [current]

  def heuristic_cost_estimate(self, start, finish, current):
    start_position = self.nodes[start].position
    finish_position = self.nodes[finish].position
    line = start_position.lat, start_position.lon, finish_position.lat, finish_position.lon
    position = self.nodes[current].position
    return self.dist2line(position.lat, position.lon, line)

  """from http://stackoverflow.com/questions/849211/shortest-distance-between-
  a-point-and-a-line-segment"""
  def dist2line2(self, x,y,line):
    x1,y1,x2,y2=line
    vx = x1 - x
    vy = y1 - y
    ux = x2-x1
    uy = y2-y1
    length = ux * ux + uy * uy
    det = (-vx * ux) + (-vy * uy) #//if this is < 0 or > length then its outside the line segment
    if det < 0:
      return (x1 - x)**2 + (y1 - y)**2
    if det > length:
      return (x2 - x)**2 + (y2 - y)**2
    det = ux * vy - uy * vx
    return det**2 / length
  def dist2line(self,x,y,line): return math.sqrt(self.dist2line2(x,y,line))

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
      available = Util.get_subdict(distances, unvisited)
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
    #print(previous)
    return distances, path

class Util:
  @staticmethod
  def get_subdict(d, keys, default=None):
    return dict([ (k, d.get(k, default)) for k in keys ])
