import mysql.connector
from mysql.connector import Error
import os

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", 3306)),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "Dantas@9293"),
                database=os.getenv("DB_NAME", "hospital")
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
