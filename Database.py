import mysql.connector

def create_database(self):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    c = conn.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS reg_db")
    conn.commit()
    conn.close()

def create_table(self):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reg_db"
    )
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uid INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(50),
            username VARCHAR(50),
            password_hash VARCHAR(255)
        )
    """)
    conn.commit()
    conn.close()

def on_start(self):
    # Open the database connection when the app starts
    self.create_database()
    self.create_table()
    self.connect_database()

def on_stop(self):
    # Close the database connection when the app stops
    self.close_database()

def connect_database(self):
    self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reg_db"
    )
    self.c = self.conn.cursor()

def close_database(self):
    if self.conn:
        self.conn.close()