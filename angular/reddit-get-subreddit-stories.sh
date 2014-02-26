awk '{printf "%s.json", $1}' | xargs -0 curl | jq '.data.children[].data | {title, url, ups, downs}' | sed 's/}/},/'
