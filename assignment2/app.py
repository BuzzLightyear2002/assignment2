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

def create_table():
    try:
        cursor = mydb.cursor()
        cursor.execute("""
        drop table products
        """)
        mydb.commit()
        cursor.close()
        return "Table 'products' created successfully or already exists."
    except Exception as e:
        return f"An error occurred while creating the table: {e}"

# Ensure the table is created at the start of the application
validation_message = create_table()
print(validation_message)  # Print the validation message


if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
