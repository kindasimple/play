curl --include http://www.reddit.com/r/random.json | grep -oE 'Location: .*' | sed 's/Location: //' | tr -d '\r' | awk '{printf "%s.json", $1}' | xargs -0 curl | jq '.data.children[].data | {title, url}'
