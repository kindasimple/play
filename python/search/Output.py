import csv
from search import *

class CSVFile:
  def __init__(self, filename):
    self.filename = filename

  def write(self, nodes, path_list):
    f = open(self.filename, 'w', newline='')
    wr = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    wr.writerow(['name','latitude','longitude', 'iconName'])
    format_ = Format()
    for node in nodes:
      wr.writerow([node.name, node.position.lat, node.position.lon, format_.placemark_node_icon])
    for algorithm in list(path_list):
      for node in path_list[algorithm]:
        icon = format_.placemark_path_icon
        if node is path_list[algorithm][0] or node is path_list[algorithm][-1]:
          icon = format_.placemark_bound_icon
        wr.writerow([node.name, node.position.lat, node.position.lon, icon])
    f.close()

class KMLFile:
  def __init__(self, filename):
    self.filename = filename

  def write(self, nodes, path_list):
    kml = Format().generate_kml(nodes, path_list)
    f = open(self.filename, 'w', newline='')
    f.write(kml)
