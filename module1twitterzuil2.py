# Connect to database
import psycopg2


def posttodb(var_bericht,var_station):

    # -----------------------------------------------------------------
    # connect to the db
    con = psycopg2.connect(
        host="localhost",  # host upon which i run the database
        database="TwitterPaal",  # database name
        user="postgres",  # username standard=postgres
        password="algra50"  # password from installation
    );
    # port = 5432 runs standard only needed if port is changed
    cur = con.cursor()
    insert_query = ''' INSERT INTO tweets (bericht, station) VALUES var_bericht, var_station'''
    cur.execute(insert_query)
    con.commit()
    print('1 record inserted correctly')
    cur.close()
    con.close()
    return

#Start Module1:
def nieuw_bericht(klant_naam, station, bericht):
    if len(bericht) > 140:
        return "Uw bericht is " + str(len(bericht) - 140) + " tekens te lang!"
    else:
        if len(klant_naam) == 0:
            klant_naam = "Anoniem"
        posttodb(bericht, station)

        return "Uw bericht is in ontvangst genomen."


# -----------------------------------------------------------------
# # retrieve data
# cur.execute('SELECT * from tweets')
# record = cur.fetchall()
# print('fetchall result: ', record)
