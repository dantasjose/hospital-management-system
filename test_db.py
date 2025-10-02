from utils.db import Database

def test_connection():
    try:
        db = Database()
        result = db.fetchall("SHOW TABLES;")
        print("✅ Conexão bem-sucedida!")
        print("Tabelas existentes no banco hospital:")
        for row in result:
            print("-", list(row.values())[0])  # pega o nome da tabela
    except Exception as e:
        print("❌ Erro ao conectar:", e)

if __name__ == "__main__":
    test_connection()
