import tweepy as tw
import os
import redis as rd
from dotenv import load_dotenv, find_dotenv



BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


redis_db = rd.StrictRedis(host="localhost", port=6379, db=0)
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)
search_words = "#felizsabado"
date_since = "2019-02-23"


public_tweets = api.home_timeline()
trending_topic = tw.Cursor(api.search,q=search_words, lang="es", since=date_since).items(5)

for tweet in trending_topic:
	tw_new_key = tweet.user.id
	tw_dict = {}
	tw_dict[tweet.text] = tw_new_key
	redis_db.zadd("tweets", tw_dict)
	print tweet.user.id
	#redis_db.set("app-twitter",tweet.text)

