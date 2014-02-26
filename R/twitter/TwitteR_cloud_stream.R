#install.packages("streamR")
library(ROAuth)
library(streamR)
library(tm)
library(wordcloud)
library(RColorBrewer)
library(streamR)
library(rjson)

credFile <- "~/Documents/github/play/R/twitter/cred.RData"

requestURL <- "https://api.twitter.com/oauth/request_token"
# accessURL <- "https://api.twitter.com/oauth/access_token"
# authURL <- "https://api.twitter.com/oauth/authorize"
# consumerKey <- "N1HPLttkyCQVEijmIqwmUg"
# consumerSecret <- "RiF64TMKajwgGKxYHyMCgAEGBjT0iCoxVZ45cYkR9us"
# 
# twitCred <- OAuthFactory$new(consumerKey=consumerKey,
#                              consumerSecret=consumerSecret,
#                              requestURL=requestURL,
#                              accessURL=accessURL,
#                              authURL=authURL)
# twitCred$handshake()
# # 
# 
# save(twitCred, file=credFile)

load(credFile)
payloadUri <- './twitter-stream.json'

keywords <- c("java", "wp7", "win8", "scala", "hackathon")
locations <- c(-81.3027,28.2053,-81.1339,28.3651)
tweet.count <- 5

unlink(payloadUri)
filterStream(payloadUri, track=keywords, locations=locations, language="en"
             , tweets=tweet.count, oauth=twitCred)

payload <- readLines(payloadUri)
document <- unlist(lapply(payload, function(x) fromJSON(x, method='C')$text))
scrubbed_text = iconv(document, from = "ASCII", to = "utf-8", sub="")

# create a corpus
scrubbed_corpus = Corpus(VectorSource(scrubbed_text, encoding = "UTF-8"))

# create document term matrix applying some transformations
tdm = TermDocumentMatrix(scrubbed_corpus
                         , control = list(removePunctuation = TRUE
                                          , stopwords = c(stopwords("english"))
                                          , removeNumbers = TRUE, tolower = TRUE))

# define tdm as matrix
m = as.matrix(tdm)
# get word counts in decreasing order
word_freqs = sort(rowSums(m), decreasing=TRUE) 
# create a data frame with words and their frequencies
dm = data.frame(word=names(word_freqs), freq=word_freqs)

# plot wordcloud
wordcloud(dm$word, dm$freq, random.order=FALSE, colors=brewer.pal(8, "Dark2"))

# save the image in png format
png(sprintf("twitter_cloud_%s.png", paste(keywords, collapse="-")), width=12, height=8, units="in", res=300)
wordcloud(dm$word, dm$freq, random.order=FALSE, colors=brewer.pal(8, "Dark2"))
dev.off()

