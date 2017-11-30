# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: twitter crawler (Old Data), Created Jul. 2017
Ver 1.2 (finish)
Link: 
https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
'''
# --------------------------------------------------- lib import
import tweepy
from tweepy import OAuthHandler
import json
# --------------------------------------------------- credential settings
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
# --------------------------------------------------- program
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, 
					wait_on_rate_limit_notify=True)
# Has a daytime limit up to recent two weeks
since = '2017-01-01'
until = '2017-01-15'
querylist = ['Donald Trump', 'Apple Inc']
# --------------------------------------------------- activate
for i in querylist:
	for tweet in tweepy.Cursor(api.search, q=i, since=since, until=until, lang="en").items():
		js = tweet._json
		try:
			# filter language
			if js['user']['lang'] == 'en':
				user = js['user']
				dic = {
					"time": js['created_at'],
					"content": js['text'],
					"profile": {
						'id': user['id'],
						'name': user['name'],
						'tweetName': user['screen_name'],
						'location': user['location'],
						'info': user['description'],
						'followers': user['followers_count'],
						'friends': user['friends_count'],
						'list': user['listed_count'],
						'fav': user['favourites_count'],
						'stat': user['statuses_count'],
						'create': user['created_at'],
						'time_zone': user['time_zone'],
						'lang': user['lang']
						},
					"tags": js['entities']['hashtags'],
					"symbols": js['entities']['symbols'],
					"urls": js['entities']['urls']
					}

				# -- Compile jsonarray --
				jsonarray = json.dumps(dic)

				# -- Determine directory to save file --
				file = 'out_old.json'
				print('-- JSON will be saved in {} --'.format(file))

				# -- Save jsonarray into selected file--
				with open(file, 'a') as f:
					f.write(jsonarray + '\n')
					print("GET ONE OUTCOME: {}".format(tweet.created_at))
		except Exception as e:
			print(e)