# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: twitter crawler (Stream), Created June. 2017
Ver 1.7 (tweet crawler tweepy version)
Link: 
'''
# --------------------------------------------------- lib import
import json

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from http.client import IncompleteRead
# --------------------------------------------------- program
class MyListener(StreamListener):
	# -- action on process --
	def on_status(self, status):
		js = status._json
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
			file = 'out.json'
			print('-- JSON will be saved in {} --'.format(file))

			# -- Save jsonarray into selected file--
			with open(file, 'a') as f:
				f.write(jsonarray + '\n')
				print("GET ONE OUTCOME: {}".format(js['created_at']))

	# -- action on error --
	def on_error(self, status_code):
		print("Encountered error with status code: ", status_code)
		return True
	# -- action on timeout --
	def on_timeout(self):
		print(sys.stderr, "Timeout...")
		return True
# --------------------------------------------------- credential settings
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
# --------------------------------------------------- program start
if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	while True:
	    try:
	        # Connect/reconnect the stream
	        print('-- tweepy is running --')
	        streamingAPI = Stream(auth, MyListener())
	        # -- filter --
	        querylist = ['Donald Trump', 'Apple Inc']
	        streamingAPI.filter(track=querylist)
	    except IncompleteRead:
	        continue
	    except KeyboardInterrupt:
	        streamingAPI.disconnect()
	        break
	
    