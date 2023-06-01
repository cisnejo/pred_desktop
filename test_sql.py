import os
import time
from dotenv import load_dotenv
import mysql.connector


# Connect to the database
load_dotenv()
print(time)
MYSQL_PW = os.getenv("MYSQL_PW")

db = mysql.connector.connect(
    host="127.0.0.1", user="root", password=MYSQL_PW, database="pred"
)


# Create a cursor to execute SQL queries
cursor = db.cursor()

# Insert data into MATCHDATA table

query = "SELECT * FROM PLAYERMATCHDATA where playerName = %s"
cursor.execute(query,("loki",))
result = cursor.fetchall()
print(result)
