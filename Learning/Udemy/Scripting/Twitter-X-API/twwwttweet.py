import tweepy
import tweepy.cursor
import time

# Now twitter has paid API so I have not created API App
auth = tweepy.OAuth1UserHandler(
  # consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

# Genrous Bot
# API hit limit handler
def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)

# # Get followers name list
# for follower in limit_handler(tweepy.cursor(api.followers).items()):
#   print(follower.name)
#   if follower.name == 'masoom2206':
#     follower.follow()
#     break

# search a word in tweet and like/favorite that tweet
search_string = 'python'
numberOfTweet = 2

for tweet in tweepy.cursor(api.search, search_string).items(numberOfTweet):
  try:
    tweet.favorite()# Like
    # tweet.retweet()# ReTweet
    print("I like that tweet!")
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
