import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="heri123",
        database="novel"
    )
