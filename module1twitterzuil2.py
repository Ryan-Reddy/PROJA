# Connect to database
import psycopg2

# -----------------------------------------------------------------
# connect to the db
con = psycopg2.connect(
    host = "localhost",         #host upon which i run the database
    database = "TwitterPaal",  #database name
    user = "postgres",          #username standard=postgres
    password = "algra50"       #password from installation
)
    # port = 5432 runs standard only needed if port is changed

#Start Module1:
def nieuw_bericht(klant_naam, station, bericht):
    if len(bericht) > 140:
        return "Uw bericht is " + str(len(bericht) - 140) + " tekens te lang!"
    else:
        if len(klant_naam) == 0:
            klant_naam = "Anoniem"
        tweets = open("tweets.txt", "a")
        tweets.write(str(klant_naam+" schreef: " + bericht +" op station: " + station + "\n"))
        tweets.close()
        return "Uw bericht is in ontvangst genomen."

# -----------------------------------------------------------------
#
# executing a sql to instert data:
cur = con.cursor()
insert_query = ''' INSERT INTO tweets (bericht, klant_id_fk, station) VALUES ('herro', 1, 'Schiermonnikoog')'''
cur.execute(insert_query)


# insert_query2 = ''' INSERT INTO gebruiker (ID, NAME, PRICE) VALUES (2, 'Opa', 400)'''
# insert_query3 = ''' INSERT INTO gebruiker (ID, NAME, PRICE) VALUES (3, 'mom', 2455)'''
# cur.execute(insert_query2)
# cur.execute(insert_query3)

con.commit()
print('1 record inserted correctly')
-----------------------------------------------------------------
# retrieve data
cur.execute('SELECT * from tweets')
record = cur.fetchall()
print('fetchall result: ', record)


cur.close()
con.close()
