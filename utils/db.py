import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Dantas@9293",
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
        try:
            if hasattr(self, "cursor") and self.cursor:
                self.cursor.close()
            if hasattr(self, "conn") and self.conn and self.conn.is_connected():
                self.conn.close()
        except:
         pass  # ignora qualquer erro ao finalizar
