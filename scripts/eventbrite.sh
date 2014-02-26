curl -vs "https://www.eventbrite.com/json/event_search?app_key=56YGKM2N6D456IRI27&postal_code=32839" | jq '.events[].event | { description,url,title, start: .start_date, }'
