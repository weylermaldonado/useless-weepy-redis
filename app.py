
import redis as rd


# Config

redis_db = rd.StrictRedis(host="localhost", port=6379, db=0)



print("---------------------Mostrando los tweets en orden ascendente segun su ID de usuario:----------------------")
asc_tweets = redis_db.zrange("tweets", 0, -1) 

for element in asc_tweets:
	print element

print("---------------------Mostrando los tweets en orden descendente segun su ID de usuario:---------------------")
desc_tweets = redis_db.zrange("tweets", 0, -1, desc=True) 

for element in desc_tweets:
	print element
