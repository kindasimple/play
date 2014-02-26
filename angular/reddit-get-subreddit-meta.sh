awk '{printf "%sabout.json", $1}' | xargs -0 curl | jq '.data | {name: .display_name, title, subscribers, created, url, description}'
