outfile=reddit.js
./reddit-get-subreddit-random.sh > subreddit.tmp
echo "function RedditCtrl(\$scope) { \$scope.subreddit = " > ${1:-$outfile}
./reddit-get-subreddit-meta.sh < subreddit.tmp >> ${1:-$outfile}
echo ";" >> ${1:-$outfile}
echo "\$scope.stories = [" >> ${1:-$outfile}
./reddit-get-subreddit-stories.sh < subreddit.tmp >> ${1:-$outfile}
echo "];}" >> ${1:-$outfile}
rm subreddit.tmp
