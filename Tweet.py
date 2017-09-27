import tweepy


class Tweet:

	topic = ""

	def __init__(self,topic):
		self.topic = topic

	def getTweets(self):
		c_key = 'mXwXLfzipnRTgq1WpZdzfIKvl'
		c_secret = '3onhLpaY6YPfLq53Pns0Bb7fj6WXiSNKYceSfaOiTGylUFpiTL'
		a_token = '2972156527-zl2XpdY9UEzjUmZmXgrjVJNmkfgv8Ky3f4SpRRE'
		a_secret = 'OEZohRHaw70KjL5XdNwrstnrLzoEYkrF2UGYN2Gde8DxP'

		auth = tweepy.OAuthHandler(c_key,c_secret)
		auth.set_access_token(a_token,a_secret)
		twitter_api = tweepy.API(auth)
		public_tweets = twitter_api.search(q = self.topic, count = 100)
		return public_tweets
