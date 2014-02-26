curl --include http://www.reddit.com/r/random.json | grep -oE 'Location: .*' | sed 's/Location: //' | tr -d '\r'
