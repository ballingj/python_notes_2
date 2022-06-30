#3 All of 01 and 02 plus joining multiple tables

import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute(
    "create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "State of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "State of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
]

city_list = [
    ("Liberty City", "New York"),
    ("state of New Guernsey", "state of New Jersey"),
    ("Anywhere, USA", "all USA cities"),
    ("Vice City", "Miami"),
    ("state of San Andreas", "state of California"),
    ("Los Santos", "Los Angeles")
]

# Create database table "gta" and insert the values in release_list
cursor.executemany("insert into gta values (?,?,?)", release_list)
# save changes immediatley
connection.commit()

#print database rows
for row in cursor.execute("select * from gta"):
    print(row)

print("*" * 50)  # separator

#print specific rows : city = "Liberty City"
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

# create a second table called cities using cities_list
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.executemany("insert into cities values (?,?)", city_list)
# save changes immediatley
connection.commit()

# select only the rows where gta_city=Liberty City
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

# combine data from 2 tables and manipulate it : changing "Liberty City" to "New York"
print("*" * 50)
for i in gta_search:
    #replace every instance of "Liberty City" with "New York"
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)

#close the database connection
connection.close()
