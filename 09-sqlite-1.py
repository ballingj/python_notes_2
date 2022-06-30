# This is the minimum code required to create a sqlite database; the db will be empty

import sqlite3

connection = sqlite3.connect("gta.db")

release_list = [
    (1997, "Grand Theft Auto", "State of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "State of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
]

connection.close()