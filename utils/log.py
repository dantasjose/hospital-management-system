from utils.db import Database
from tabulate import tabulate

class Logs:
    def __init__(self):
        self.db = Database()

    def registrar_log(self, entidade, acao, detalhes=""):
        """Registra uma ação no banco de dados"""
        self.db.execute(
            "INSERT INTO logs (entidade, acao, detalhes) VALUES (%s, %s, %s)",
            (entidade, acao, detalhes)
        )
        print(f"📝 Log registrado: {entidade} - {acao}")

    def listar_logs(self, limit=20):
        """Lista os últimos logs"""
        logs = self.db.fetchall(
            "SELECT id, entidade, acao, detalhes, data_hora FROM logs ORDER BY data_hora DESC LIMIT %s",
            (limit,)
        )
        if not logs:
            print("⚠️ Nenhum log encontrado.")
            return
        print("\nÚltimas ações registradas:")
        print(tabulate(logs, headers="keys", tablefmt="fancy_grid"))

    def limpar_logs(self):
        """Apaga todos os logs (cuidado!)"""
        confirmar = input("Tem certeza que deseja apagar todos os logs? (s/n): ").lower()
        if confirmar == "s":
            self.db.execute("DELETE FROM logs")
            print("✅ Todos os logs foram apagados.")
        else:
            print("❌ Operação cancelada.")
