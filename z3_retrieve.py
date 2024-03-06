import sqlite3

conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()

# Retrieve list of all tables from our database
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cr.fetchall()
print("list of tables in the DB file:\n",tables,"\n")

# Get all columns from movies table
cr.execute("PRAGMA table_info({});".format("movies"))
columns = cr.fetchall()
column_names = [column[1] for column in columns]
print("list of column names in the DB file:\n",column_names,"\n")

cr.execute('''SELECT * FROM movies''')
print(cr.fetchall())
