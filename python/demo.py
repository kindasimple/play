#!/usr/bin/python

from maths import Arithmetic, Number

print("Do some arithmetic")
print("2 + 3 = %d" % Arithmetic().Add(Number(2), Number(3)).value)
print("8 - 3 = %d" % Arithmetic().Subtract(Number(8), Number(3)).value)
print("4 * 5 = %d" % Arithmetic().Multiply(Number(4), Number(5)).value)
print("16 / 4 = %d" % Arithmetic().Divide(Number(16), Number(4)).value)

print("Equality Tests")
print("2 == 2 is %s" % Arithmetic().Equals(Number(2), Number(2)))
print("1 == 2 is %s" % Arithmetic().Equals(Number(1), Number(2)))

from search import *

def print_graph_details(algorithm):
  print("Vertices: ")
  for n in algorithm.nodes:
    v = algorithm.nodes[n]
    print("{}: {} ({},{})".format(v.id, v.name, v.position.lat, v.position.lon))
  print("Edges: ")
  for a in algorithm.graph:
    e = algorithm.graph[a]
    print("[{}] {} ".format(algorithm.nodes[a].id, algorithm.nodes[a].name), e)



import time
try_again = True
while try_again:
  try_again = False

  algorithm = Backtrack()
  print_graph_details(algorithm)
  start = list(algorithm.nodes)[0]
  finish = list(algorithm.nodes)[-1]

  try:
    start_time = time.clock()
    print("Solution via Backtracking: {result} [{elapsed}]".format(result = algorithm.search(start, finish), elapsed = time.clock() - start_time))
    algorithm = Dijkstra(algorithm.nodes, algorithm.graph)
    start_time = time.clock()
    print("Solution via Dijkstra: {result} [{elapsed}]".format(result = algorithm.search(start, finish)[1], elapsed = time.clock() - start_time))
    algorithm = AStar(algorithm.nodes, algorithm.graph)
    start_time = time.clock()
    print("Solution via A*: {result} [{elapsed}]".format(result = algorithm.search(start, finish), elapsed = time.clock() - start_time))
  except SearchError:
    print("No solution to random data set. Retrying")
    try_again = True

var = input("Run Search Speed Test: [y/n]")
while var is not 'y' and var is not 'n':
  var = input("Run Search Speed Test: [y/n]")

nodes = 100
while(nodes < 1000 and var is 'y'):
  print("Searching a Graph with {} nodes".format(nodes))
  algorithm = Backtrack()
  connectivity = 1 / (2 + math.sqrt((nodes - 100)))
  algorithm.generate_graph(nodes, connectivity)
  print("connectivity ", connectivity)

  start = list(algorithm.nodes)[0]
  finish = list(algorithm.nodes)[-1]

  print("Start: {}, Finish: {}".format(algorithm.nodes[start], algorithm.nodes[finish]))

  start_time = time.clock()
  print("Solution via Backtracking: {result}  [{elapsed}]".format(result = algorithm.search(start, finish), elapsed = time.clock() - start_time))
  algorithm = Dijkstra(algorithm.nodes, algorithm.graph)

  start_time = time.clock()
  print("Solution via Dijkstra: {result}  [{elapsed}]".format(result = algorithm.search(start, finish)[1], elapsed = time.clock() - start_time))

  start_time = time.clock()
  algorithm = AStar(algorithm.nodes, algorithm.graph)
  print("Solution via A*: {result} [{elapsed}]".format(result = algorithm.search(start, finish), elapsed = time.clock() - start_time))
  nodes = math.floor(nodes * 1.1)

#print("Get some projects from Github")
#from github_demo import github_list_repo
