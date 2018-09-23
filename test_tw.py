import time
from TwitterSearch import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re

def filterTweet(string):
	
	try:
		while(True):
			if('http' in string):
				string = string.split('http')[0]
				
				#string = re.search(r'.+(?=http.+)', string)[0]
				#import pdb; pdb.set_trace()
			elif('RT' in string):
				string = re.search(r'(?<=RT).+', string)[0]
			else:
				break
	except:
		pass
	return string

try:
	tso = TwitterSearchOrder()
	tso.set_keywords(['nike'])
	tso.set_language('en')
	ts = TwitterSearch(
						consumer_key = '5q9xjxFsTXXuz0DWiyJC3WcSR',
						consumer_secret = 'XptkBaaSUHFwF9lVfce1M51JmZZQElLxQ8ZO3T80rhI0fjVydK',
						access_token = '189953925-xCzkiZE7A2N8jejnO0poO372qqGSriAcFaZjOGF0',
						access_token_secret = 'qxvgonMEav4yHBKtdC8gXtOlI4S0VqlCveFpK7hmDu2hF'
						)
    
	#for tweet in ts.search_tweets_iterable(tso):
	#	print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
	#print(len(ts.search_tweets_iterable(tso)))

	sleep_for = 10 # sleep for 60 seconds
	last_amount_of_queries = 0 # used to detect when new queries are done

	analyzer = SentimentIntensityAnalyzer()
	
	for tweet in ts.search_tweets_iterable(tso):
		vs = analyzer.polarity_scores(tweet['text'])
		
		
		#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
		
		
		tweet_text = filterTweet(tweet['text'])
		#import pdb; pdb.set_trace()
		print("{:-<65} {}".format(tweet_text, str(vs)))
		
		#import pdb; pdb.set_trace()
		#queries, tweets_seen = current_ts_instance.get_statistics()
		
		current_amount_of_queries = ts.get_statistics()[0]
		if not last_amount_of_queries == current_amount_of_queries:
			last_amount_of_queries = current_amount_of_queries
			time.sleep(sleep_for)
	
	
except TwitterSearchException as e: # take care of all those ugly errors if there are some
	print(e)	
	

	



