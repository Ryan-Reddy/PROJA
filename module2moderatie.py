#Start Module2:

def tweet_keuren(berichtOK):
    tweets = open("tweets.txt", "r")
    temptweet = tweets.readline()
    tweets.close()
    # berichtOK = input("Is het bericht goedgekeurd? ja/nee: ").lower()
    if berichtOK == "ja":
        tweets = open("tweets.txt", "r")
        print("Bericht: \n" + tweets.readline() + "is goedgekeurd")
        tweets.close()
        with open("tweets.txt", "r") as ob:
            zinnen = ob.readlines()
            ptr = 1
            with open("tweets.txt", "w") as nb:
                for zin in zinnen:
                    if ptr != 1:
                        nb.write(zin)
                    ptr += 1
        goedgekeurde_tweets = open("goedgekeurde_tweets.txt", "a")
        goedgekeurde_tweets.write(str(temptweet) + "\n")
        goedgekeurde_tweets.close()
        return exit()

    elif berichtOK == "nee":
        tweets = open("tweets.txt", "r")
        print("Bericht: \n" + tweets.readline() + "is afgekeurd")
        tweets.close()
        with open("tweets.txt", "r") as ob:
            zinnen = ob.readlines()
            ptr = 1
            with open("tweets.txt", "w") as nb:
                for zin in zinnen:
                    if ptr != 1:
                        nb.write(zin)
                    ptr += 1
        afgekeurde_tweets = open("afgekeurde_tweets.txt", "a")
        afgekeurde_tweets.write(str(temptweet) + "\n")
        afgekeurde_tweets.close()
        return exit()

    else:
        return "ongeldige input"
def readnexttweet():
    tweets = open("tweets.txt", "r")
    nexttweet=tweets.readline()
    tweets.close()

    return nexttweet

# print(tweet_keuren())