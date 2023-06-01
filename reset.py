import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('new.db')
cursor = connection.cursor()

# Get a list of all table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Iterate over each table and delete all rows
for table in tables:
    table_name = table[0]
    cursor.execute(f"DELETE FROM {table_name}")

# Commit the changes and close the connection
connection.commit()
connection.close()