library(googleVis)
weightRange=c(100, 220)
fatRange=c(.05,.3)
##par(mfrow=c(2,1))
par(mfrow=c(2,2))

#Plot Kelly's Data
obs <- read.csv("./KG NYE Challenge - Kelly.csv")
obs$Date <- as.Date(obs$Date, format="%m/%d/%Y")
obs.kelly <- obs
obs.kelly$person = 'kelly'


plot(Target.Weight ~ Date, obs, type = "l", main = "Kelly Recorded Weight over time",ylim=weightRange)
lines(Recorded.Weight ~ Date, obs, type="l", col = "red") 
abline(lm(Recorded.Weight ~ Date, obs), col = "blue")

plot(Target.Bodyfat.. ~ Date, obs, type = "l", main = "Kelly Recorded Bodyfat over time",ylim=fatRange)
lines(Recorded.Bodyfat ~ Date, obs, type="l", col = "red")
abline(lm(Recorded.Bodyfat ~ Date, obs), col = "blue")

## Plot Evan's Data
obs <- read.csv("./KG NYE Challenge - Evan.csv")
obs$Date <- as.Date(obs$Date, format="%m/%d/%Y")
obs.evan <- obs
obs.evan$person <- "evan"

plot(Target.Weight ~ Date, obs, type = "l", main = "Evan Recorded Weight over time",ylim=weightRange)
lines(Recorded.Weight ~ Date, obs, type="l", col = "red") 
abline(lm(Recorded.Weight ~ Date, obs), col = "blue")


plot(Target.Bodyfat.. ~ Date, obs, type = "l", main = "Evan Recorded Bodyfat over time",ylim=fatRange)
lines(Recorded.Bodyfat ~ Date, obs, type="l", col = "red")
abline(lm(Recorded.Bodyfat ~ Date, obs), col = "blue")

## Calorie data
#plot(Observed.Accumulated.Weight.Error ~ Date, obs, type = "l", main = "Evan Dieting Error over time", ylim=range(obs$Observed.Accumulated.Weight.Error, na.rm=TRUE))


## Plot with googleVis
drops <- c("Calorie.Target","Calories.In", "Daily.Calories", "Exercise", "Calorie.Expenditure", "Dieting.Error", "Expected.Weight.Change", "Accumulated.Expected.Weight.Change", "Expected.Bodyfat.Change", "Observed.Accumulated.Weight.Error")
obs.evan <- obs.evan[,!(names(obs.evan) %in% drops)]

data <- rbind(obs.kelly, obs.evan)
data$Day <- sapply(as.character(data$X.1), function(x){
  as.numeric(unlist(strsplit(x, " "))[2])
})
data <- data[, !(names(data) == "X.1")]
d <- gvisMotionChart(data,
    idvar="person", timevar="Date",
    xvar="Recorded.Weight", yvar="Recorded.Bodyfat", date.format = '$m/%d',
    colorvar="Day", sizevar="Recorded.Weight",
    options=list(width=700, height=600))

plot(d)
