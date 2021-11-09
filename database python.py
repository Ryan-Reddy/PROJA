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
# -----------------------------------------------------------------
cur = con.cursor()
#
# executing a sql to instert data:
insert_query = ''' INSERT INTO tweets (ID, NAME, PRICE) VALUES (1, 'Ryan', 1200)'''
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