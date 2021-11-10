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
def modifystatustweet(berichtOK, mod_name):
    print('berichtok = ',berichtOK)
    print('modnum= ', mod_name)
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50")  # password from installation
    cur = con.cursor()

    # insert modname into moderator(moderator_id)
    insert_query = '''INSERT INTO moderator(moderator_name) VALUES (%s) RETURNING moderator_id;'''
    record_to_insert = (mod_name),
    cur.execute(insert_query, record_to_insert)
    new_mod_id = cur.fetchone()
    print(new_mod_id)

    # fetch tweetnumber next unmoderated tweet
    cur.execute('''SELECT tweet_number FROM tweets WHERE tweet_status = 0 LIMIT 1''')
    record = cur.fetchone()
    record_in_use = record[0]

    if berichtOK == "ja":
        insert_query_update_stat_yes = '''UPDATE tweets SET tweet_status = (%s) WHERE tweet_number = (%s);'''
        record_to_insert_stat_yes = (2,record_in_use)

        cur.execute(insert_query_update_stat_yes, record_to_insert_stat_yes)

        con.commit()

        insert_query_update_moddate = '''UPDATE tweets SET moderation_date = CURRENT_TIMESTAMP WHERE tweet_number = %s;'''
        cur.execute(insert_query_update_moddate % (record_in_use))
        con.commit()

        insert_query = '''UPDATE tweets SET moderator_id_fk = %s WHERE tweet_number = %s; '''
        record_to_insert = (new_mod_id, record_in_use)
        cur.execute(insert_query, record_to_insert)
        con.commit()

        cur.close()
        con.close()
        print('tweet goedgekeurd')
        return exit()

    elif berichtOK == "nee":
        insert_query_update_stat_no = '''UPDATE tweets SET tweet_status = (%s) WHERE tweet_number = (%s);'''
        record_to_insert_stat_no = (1, record_in_use)

        cur.execute(insert_query_update_stat_no, record_to_insert_stat_no)

        con.commit()

        insert_query_update_moddate = '''UPDATE tweets SET moderation_date = CURRENT_TIMESTAMP WHERE tweet_number = %s;'''
        cur.execute(insert_query_update_moddate % (record_in_use))
        con.commit()

        insert_query = '''UPDATE tweets SET moderator_id_fk = %s WHERE tweet_number = %s; '''
        record_to_insert = (mod_name, record_in_use)
        cur.execute(insert_query, record_to_insert)
        con.commit()

        cur.close()
        con.close()
        print('tweet goedgekeurd')
        return exit()

    cur.close()
    con.close()

    return print('yellow')
