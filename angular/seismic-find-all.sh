mongoexport --db usgs --collection 4.5_day | jq "{id, geometry} + {mag: .properties.mag}" | sed -e 's/^.*}$/},/'
