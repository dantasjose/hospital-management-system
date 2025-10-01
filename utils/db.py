import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sua_senha",
                database="hospital"
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("✅ Conectado ao MySQL com sucesso!")
        except Error as e:
            print(f"❌ Erro de conexão: {e}")

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def fetchall(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
