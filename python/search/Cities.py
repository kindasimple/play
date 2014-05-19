#!/usr/bin/python
import math

class Position :
  def __init__(self, lat, lon) :
    self.lat = lat
    self.lon = lon
  def __str__(self):
    return str(self.lat) + ", " + str(self.lon)
  def __repr__(self):
    return str(self.lat) + ", " + str(self.lon)

class City :
  def __init__(self, id, name, position) :
    self.id = id
    self.name = name
    self.position = position
  def __str__(self):
    return "{} ({},{})\n".format(self.name, str(self.position.lat), str(self.position.lon))
  def __repr__(self):
    return "\n{} ({},{})\n".format(self.name, str(self.position.lat), str(self.position.lon))

  def get_distance(self, other) :
    return math.sqrt(math.pow(self.position.lat-other.position.lat, 2) + math.pow(self.position.lon-other.position.lon, 2))
