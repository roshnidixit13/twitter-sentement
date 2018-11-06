import tweepy


class Tweet:

	topic = ""

	def __init__(self,topic):
		self.topic = topic

	def getTweets(self):
		c_key = ''
		c_secret = ''
		a_token = ''
		a_secret = ''

		auth = tweepy.OAuthHandler(c_key,c_secret)
		auth.set_access_token(a_token,a_secret)
		twitter_api = tweepy.API(auth)
		public_tweets = twitter_api.search(q = self.topic, count = 100)
		return public_tweets
