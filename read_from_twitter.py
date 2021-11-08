from TwitterAPI import TwitterAPI

from auth import (
    Consumer_Key,
    Consumer_Key_Secret,
    Access_Token,
    Access_Token_secret
)

consumer_key = Consumer_Key
consumer_secret = Consumer_Key_Secret
access_token_key = Access_Token
access_token_secret = Access_Token_secret


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def grabtweets():

    r = api.request('statuses/home_timeline', {'count':50})
    for item in r.get_iterator():
        # print(item)
        dict ={}
        if 'user' and 'text' in item:
            tweet = item['text']
            # print(item['text'])
            return tweet
    #     print(item['user'])



# Get your last 50 tweets
# r = api.request('statuses/home_timeline', {'count':50})
# for item in r.get_iterator():
#     print(item)
#     if 'text' in item:
#         print(item['text'])

# ------------------------- add to a database from here