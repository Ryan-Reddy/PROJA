import psycopg2

#Start Module2:

# get info from the next unrated tweet:
def readnexttweet():
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50")  # password from installation
    cur = con.cursor()
    cur.execute('SELECT bericht , tweet_number, tweet_status FROM tweets WHERE tweet_status = 0 LIMIT 1')
    record = cur.fetchall()
    cur.close()
    con.close()
    return record[0][0]

# get the tweetnumber of the next unrated tweet, update it after choice mod:
def modifystatustweet(berichtOK, modNumEntry):
    print(berichtOK)
    print(modNumEntry)
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50")  # password from installation
    cur = con.cursor()
    cur.execute('tweet_number FROM tweets WHERE tweet_status = 0 LIMIT 1')
    record = cur.fetchall()
    print('tweetnumber', record)

    if berichtOK == "ja":
        cur.execute('tweet_number FROM tweets WHERE tweet_status = 0 LIMIT 1')
        return exit()

    elif berichtOK == "nee":
        cur.execute('tweet_number FROM tweets WHERE tweet_status = 0 LIMIT 1')
        return

    # --------------------------------------
    # update line with mod number
    # --------------------------------------


    cur.close()
    con.close()

    return exit()
