import mysql.connector


def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="elec498g7",
        database="database_v2"
    )
    return mydb
