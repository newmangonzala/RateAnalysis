import sys
import praw
import pandas as pd
import datetime as dt
import pdb
from praw.models import MoreComments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

if len(sys.argv) < 3:
	print("too few arguments, type name of subreddit");
	exit();

subreddit_name = sys.argv[1];	# name of subreddit
subreddit_query = sys.argv[2];	# search within subreddit

reddit = praw.Reddit(client_id='', \		# put your own (from https://www.reddit.com/wiki/api)
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='');
					 
subreddit = reddit.subreddit(subreddit_name);
top_subreddit = subreddit.search(subreddit_query, sort="hot", limit=5);
	
topics_dict = {"title":[], "score":[], "id":[], "url":[], "comms_num": [], "created": [], "body":[]};
	
for submission in top_subreddit:
	if submission.score > 50:
		total_score = 0;
		for comment in submission.comments:
			if isinstance(comment, MoreComments):
				continue;
			if comment.score < 50:
				continue;
			analyzer = SentimentIntensityAnalyzer();
			vs = analyzer.polarity_scores(comment.body);
			total_score = total_score + vs["compound"]*comment.score;
				
	print("final score for", submission.title, "is", str(total_score/len(submission.comments)));
			
# comments_data = pd.DataFrame(comments_dict);
# comments_data.to_csv('test2.csv', index=False);

