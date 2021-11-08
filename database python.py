import psycopg2

# connect to the db
con = psycopg2.connect(
    host = "localhost",         #host upon which i run the database
    database = "databasename",  #database name
    user = "postgres",          #username standard=postgres
    password = "postgres"       #password from installation
    # port = 5432 runs standard only needed if port is changed
)

# cursor
cur = con.cursor()


# Uitvoer query, atribuut, atribuut moet je vervangen voor de atributen die je wilt fetchen.
# zet select * from tabel om alles van een tabel te fetchen
# cur.execute("select atribuut, atribuut from tabel")
cur.execute('select id, name from employees')


# execute query

# Door de constructie met (%s, %s, %s), (attribuut, attribuut, attribuut)) zetten we alleen maar strings erin
# die we later toewijzen. Hierdoor kunnen we de database vullen zonder steeds de code aan te moeten passen.
# Deze manier is ook veiliger dan gelijk values (attribuut, attribuut, attribuut)).

cur.execute("insert into employees (id,name) values (%s, %s)", (1, "satoshi"))


# return rows
rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]}")

# commit transaction (save) to database (needed for writing to database
con.commit()


# close cursor
cur.close()

# close the conenction
con.close()