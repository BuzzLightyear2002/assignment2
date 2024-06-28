# Author - Raj Chauhan B00973860
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="assignment2-mysql.cl179oaea0jj.us-east-1.rds.amazonaws.com",
    user="admin",
    password="RAJ1972002",
    database="assignment2_db"
)

def drop_table():
    try:
        cursor = mydb.cursor()
        cursor.execute("DROP TABLE IF EXISTS products")
        mydb.commit()
        cursor.close()
        return "Table 'products' dropped successfully."
    except Exception as e:
        return f"An error occurred while dropping the table: {e}"

# Execute the drop table command
drop_message = drop_table()
print(drop_message)  # Print the drop table message

if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
