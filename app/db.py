import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="sbps2349", database="airline_db"
    )
