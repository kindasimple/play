library(rmongodb)
mongo <- mongo.create(db="usgs")
res <- mongo.find(mongo, "usgs.4.5_day")
out <- NULL
while(mongo.cursor.next(res)){ 
  out <- c(out, list(mongo.bson.to.list(mongo.cursor.value(res))))
}
