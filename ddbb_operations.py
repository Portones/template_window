import psycopg2

from consts import db_params

def connect_db():

    connection = psycopg2.connect(**db_params)
    return connection.cursor()

def execute_query(query):
    with connect_db() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
