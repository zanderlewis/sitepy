import sqlite3
import psycopg2
import mysql.connector

class Database:
    def __init__(self, db_type, name, user=None, password=None, host=None, port=None):
        if db_type == 'sqlite':
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        elif db_type == 'mysql':
            self.conn = mysql.connector.connect(user=user, password=password, host=host, database=name)
            self.cursor = self.conn.cursor()
        elif db_type == 'postgresql':
            self.conn = psycopg2.connect(database=name, user=user, password=password, host=host, port=port)
            self.cursor = self.conn.cursor()
        else:
            raise ValueError("Invalid database type")

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()
