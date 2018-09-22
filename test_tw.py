import time
from TwitterSearch import *

try:
	tso = TwitterSearchOrder()
	tso.set_keywords(['nike'])
	ts = TwitterSearch(
						consumer_key = '5q9xjxFsTXXuz0DWiyJC3WcSR',
						consumer_secret = 'XptkBaaSUHFwF9lVfce1M51JmZZQElLxQ8ZO3T80rhI0fjVydK',
						access_token = '189953925-xCzkiZE7A2N8jejnO0poO372qqGSriAcFaZjOGF0',
						access_token_secret = 'qxvgonMEav4yHBKtdC8gXtOlI4S0VqlCveFpK7hmDu2hF'
						)
    
	for tweet in ts.search_tweets_iterable(tso):
		print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
		
except TwitterSearchException as e: # take care of all those ugly errors if there are some
	print(e)	
	
	"""
    file = open("number_tweets_cities2", "w")
    new = []
    tw = 0
    for city in cities:
        
        lat = float(city[2])
        lon = float(city[3])

        tso.set_geocode(lat, lon, 20, imperial_metric=True)
        tw1 = tws(tso, ts)
        new.append(tw1 - tw)
        file.write("[city: \"{}\", state: \"{}\", tweets: {} ],\n".format(city[0], city[1], tw1 - tw))
        print(tw1 - tw)
        tw = tw1
    
    print("DONE")

    file.close()
except TwitterSearchException as e: 
    print(e)
	
	"""