from twython import Twython

# from TwitterAPI import TwitterAPI

from auth import (
    Consumer_Key,
    Consumer_Key_Secret,
    Access_Token,
    Access_Token_secret
)

def post_to_twitter():
    twitter = Twython(
        Consumer_Key,
        Consumer_Key_Secret,
        Access_Token,
        Access_Token_secret
    )

    message = 'Chancellor on brink of second bailout for banks'
    twitter.update_status(status=message)
    print("tweeted: {}s".format(message))