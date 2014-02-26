
#!/bin/bash
TDIR=`mktemp -d`

trap "{ cd - ; rm -rf $TDIR; exit 255; }" SIGINT

cd $TDIR
# do important stuff here
curl http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson > output.json

mongo --eval "db.stats()"  # do a simple harmless command of some sort

RESULT=$?   # returns 0 if mongo eval succeeds

if [ $RESULT -ne 0 ]; then
  mongod &
else
  echo "mongodb running!"
fi
mongoimport --db usgs --collection 4.5_day < output.json
cd -

rm -rf $TDIR

exit 0
