#2 This is the code required to create a sqlite database and populate with data
# also involves printing the data: all and specific

import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "State of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "State of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
]

# Create a table "gta" and insert the values in release_list
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

#close the database connection
connection.close()
