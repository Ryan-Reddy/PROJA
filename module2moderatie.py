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
    print(record)
    cur.close()
    con.close()
    return record

# get the tweetnumber of the next unrated tweet, update it after choice mod:
def modifystatustweet(berichtOK, modnum):
    print('berichtok = ',berichtOK)
    print('modnum= ',modnum)
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50")  # password from installation
    cur = con.cursor()


    insert_query = '''INSERT INTO moderator(moderator_id) VALUES (%s);'''
    record_to_insert = (modnum),
    cur.execute(insert_query, record_to_insert)





    cur.execute('''SELECT tweet_number FROM tweets WHERE tweet_status = 0 LIMIT 1''')
    record = cur.fetchone()
    print('record: ',record)
    record_in_use = record[0]
    print('rec in use',type(record_in_use),record_in_use)

    if berichtOK == "ja":
        insert_query_update_stat_yes = '''UPDATE tweets SET tweet_status = (%s) WHERE tweet_number = (%s);'''
        record_to_insert_stat_yes = (2,record_in_use)

        cur.execute(insert_query_update_stat_yes, record_to_insert_stat_yes)

        con.commit()

        insert_query_update_moddate = '''UPDATE tweets SET moderation_date = CURRENT_TIMESTAMP WHERE tweet_number = %s;'''
        cur.execute(insert_query_update_moddate % (record_in_use))
        con.commit()

        insert_query = '''UPDATE tweets SET moderator_id_fk = %s WHERE tweet_number = %s; '''
        record_to_insert = (modnum, record_in_use)
        cur.execute(insert_query, record_to_insert)
        con.commit()

        cur.close()
        con.close()
        print('tweet goedgekeurd')
        return exit()



    elif berichtOK == "nee":
        insert_query = '''update tweets set tweet_status = 1 where tweet_number = (%s);'''
        record_to_insert = int(record[0][0]),
        cur.execute(insert_query, record_to_insert)
        con.commit()
        cur.close()
        con.close()
        print('tweet afgekeurd')
        return exit()

    # --------------------------------------
    # update line with mod number
    # --------------------------------------


    cur.close()
    con.close()

    return exit()
