class Format:
  def __init__(self, placemark_node_icon = 'red_small',
              placemark_path_icon = 'blu_stars', placemark_bound_icon = 'arrow'):
    self.placemark_node_icon = placemark_node_icon
    self.placemark_path_icon = placemark_path_icon
    self.placemark_bound_icon = placemark_bound_icon

  def get_kml_placemark(self, node, style = 'normalPlacemark', icon = 'red_small'):
    template = """<Placemark>
                      <name>{name}</name>
                      <Point>
                        <coordinates>{lon},{lat},0</coordinates>
                      </Point>
                      <description>{description}</description>
                      <styleUrl>#{style}</styleUrl>
                    </Placemark>"""
    return template.format(
                          name = node.name, lon = node.position.lon,
                          lat = node.position.lat, description = icon,
                          style = style)

  def generate_kml_placemarks(self, nodes, path_list):
    placemarks = ""
    for node in nodes:
      found = False
      temp_algorithm = list(path_list.keys())[0]
      temp_path = path_list[temp_algorithm]
      if node == temp_path[0] or node == temp_path[-1]:
        placemarks += self.get_kml_placemark(node, 'downArrowIcon', self.placemark_bound_icon)
        found = True
      else:
        for path in list(path_list.values()):
          if node in path:
            placemarks += self.get_kml_placemark(node, 'highlightPlacemark', self.placemark_path_icon)
            found = True
            break
      if not found:
        placemarks += self.get_kml_placemark(node, 'normalPlacemark', self.placemark_node_icon)
    return placemarks

  def get_kml_linestrings(self, path, algorithm = '', style = 'style1'):
    template = """<Placemark>
                    <name>{name}</name>
                    <styleUrl>#{style}</styleUrl>
                    <LineString>
                      <tessellate>1</tessellate>
                      <coordinates>
                      {linestrings}
                      </coordinates>
                    </LineString>
                </Placemark>"""

    line = ""
    for p in path:
      line += "{},{},0\n".format(p.position.lon, p.position.lat)
    return template.format(linestrings = line, name = algorithm, style = style)

  def generate_kml(self, nodes, path_list):
    """Add placemarks for nodes, and linestrings for paths"""
    template = """<?xml version="1.0" encoding="UTF-8"?>
                <kml xmlns="http://www.opengis.net/kml/2.2">
                  <Document>
                    <name>Searching fake cities</name>
                      <Style id="style1">
                        <LineStyle>
                          <color>73FF0000</color>
                          <width>5</width>
                        </LineStyle>
                      </Style>
                      <Style id="style2">
                        <LineStyle>
                          <color>73GGCC00</color>
                          <width>5</width>
                        </LineStyle>
                      </Style>
                      <Style id="style3">
                        <LineStyle>
                          <color>73CC0000</color>
                          <width>5</width>
                        </LineStyle>
                      </Style>
                      <Style id="downArrowIcon">
                        <IconStyle>
                          <Icon>
                            <href>http://maps.google.com/mapfiles/kml/pal4/icon28.png</href>
                          </Icon>
                        </IconStyle>
                      </Style>
                      <Style id="normalPlacemark">
                        <IconStyle>
                          <Icon>
                            <href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href>
                          </Icon>
                        </IconStyle>
                      </Style>
                      <Style id="highlightPlacemark">
                        <IconStyle>
                          <Icon>
                            <href>http://maps.google.com/mapfiles/kml/paddle/red-stars.png</href>
                          </Icon>
                        </IconStyle>
                      </Style>
                    {}
                  </Document>
                </kml>"""
    template = template.format(self.generate_kml_placemarks(nodes, path_list) + "{}")
    color = 0
    for name in path_list:
      template = template.format(self.get_kml_linestrings(path_list[name], name, "style" + str((color%3)+1)) + "{}")
      color += 1
    return template.format("")


  def get_xml_markers(cities):
    markers = "<markers>"
    for city in cities:
      markers += "<marker lat=\"{}\" lon=\"{}\"".format(city.position.lat, city.position.lon)
    markers += "</markers>"
    return markers
