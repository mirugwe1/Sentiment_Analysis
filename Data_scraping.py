#loading variables
import tweepy  
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import numpy as np
import re 
from tweepy import OAuthHandler 
from textblob import TextBlob 

##============================================== Data Scraping ====================================================================================================================================
# Extraction Twitter API credentials
consumer_key = "****************************************"
consumer_secret = "******************************************"
access_key = "************************************************"
access_secret = "********************************************"

# Authenticating with the Twitter API using the above credentials
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Opening a CSV file to store the extracted tweets
csv_file = open('ebola_tweets_modified_5.csv', 'w')
csv_writer = csv.writer(csv_file)

# Writing the column headers for the CSV file
csv_writer.writerow(["timestamp", "user", "text", "favorite_count", "retweet_count", "location"])

# Setting the search term and the date since which to start searching
q = "ebola OR Ebola OR #ebola OR #Ebola -is:retweet"
since_date = "2022-09-20"
end_date = '2022-11-30'

# Calling the Twitter API to fetch the tweets
tweets = tweepy.Cursor(api.search_tweets, q=q, lang="en", since_id=since_date).items(10000000)


# Iterating through the tweets and write them to the CSV file
for tweet in tweets:
    # Writing the tweet to the CSV file
    csv_writer.writerow([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.favorite_count, tweet.retweet_count, tweet.user.location])

csv_file.close()