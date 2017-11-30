## Twitter crawler

Crawl twitter content via Tweepy api (Streaming or period crawl).

* Tweepy https://github.com/tweepy/tweepy

### Process steps

```
1. Apply an API token through https://developer.twitter.com/

2. Fill consumer_key, consumer_secret, access_token, access_secret fields.

(Crawler)3-1. Specify query term.

(Crawler_old)3-2. Specify query term and crawling period.

4. Start to crawl!

Ex:
python3 crawler.py

-- tweepy is running --
-- JSON will be saved in out.json --
GET ONE OUTCOME: {twitter content}
```

Feel free to leave comments, make references or star!

Jimmy Chen

2017/11