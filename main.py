from flask import Flask
from textblob import TextBlob
from Tweet import Tweet
import re
import json

app = Flask(__name__)


def Unwanted72(tweet):
	tweet = " ".join(filter(lambda x:x[0]!='#', tweet.split()))
	tweet = " ".join(filter(lambda x:x[0]!='@', tweet.split()))
	tweet = re.sub(r"http\S+", "", tweet)
	return " "+tweet

@app.route('/')
def Home():
	return "Forbidden Bro - 403"

@app.route('/<string:search_topic>')
def tweetAnalyser(search_topic):
	tweet_handler = Tweet(search_topic)
	public_tweets = tweet_handler.getTweets()

	tweet_dict = []

	for t in public_tweets:
		temp_tweet = Unwanted72(t.text)
		tweet_blob = TextBlob(temp_tweet)

		try:
			tweet_blob = tweet_blob.translate(from_lang=t.lang, to='en')
		except Exception:
			pass

		tweet_sentiment = tweet_blob.sentiment

		temp_dict = {}
		temp_dict['user'] = t.user.screen_name
		temp_dict['text'] = t.text
		temp_dict['polarity'] = tweet_sentiment.polarity
		temp_dict['subjectivity'] = tweet_sentiment.subjectivity

		tweet_dict.append(str(temp_dict))

	return json.dumps(tweet_dict)

if __name__ == "__main__":
	app.run(debug = False)
	dump()





