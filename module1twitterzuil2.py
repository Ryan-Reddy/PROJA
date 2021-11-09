# Connect to database
import psycopg2


def posttodb(klant_naam, station, bericht):
    # connect to the db
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50")  # password from installation

    # port = 5432 runs standard only needed if port is changed
    cur = con.cursor()

    # insert into klant database
    insert_query = '''INSERT INTO klant (naam) VALUES (%s) RETURNING klant_id;'''
    record_to_insert = (klant_naam),
    cur.execute(insert_query, record_to_insert)
    klant_id_new_row = cur.fetchone()[0]

    # read klant_id from klant


    # insert into tweets
    insert_query2 = '''INSERT INTO tweets (bericht, station, klant_id_fk) VALUES (%s, %s, %s);'''
    record_to_insert2 = (bericht, station, klant_id_new_row)
    cur.execute(insert_query2, record_to_insert2)

    # commit
    con.commit()
    print('1 record inserted correctly')
    cur.close()
    con.close()
    return

#Start Module1:
def nieuw_bericht(klant_naam, station, bericht):
    # if len(bericht) > 140:
    #     return "Uw bericht is " + str(len(bericht) - 140) + " tekens te lang!"
    # else:
        if len(klant_naam) == 0:
            klant_naam = "Anoniem"
        posttodb(klant_naam, station, bericht)

        return "Uw bericht is in ontvangst genomen."


# -----------------------------------------------------------------
# # retrieve data
# cur.execute('SELECT * from tweets')
# record = cur.fetchall()