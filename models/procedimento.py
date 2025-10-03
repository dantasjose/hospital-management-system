from utils.db import Database
from tabulate import tabulate
from datetime import datetime

class Procedimento:
    def __init__(self):
        self.db = Database()

    def validar_data(self, data_str):
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def cadastrar(self):
        cpf = input("Digite o CPF do paciente: ")
        paciente = self.db.fetchone("SELECT id FROM pacientes WHERE cpf = %s", (cpf,))
        if not paciente:
            print("⚠️ Paciente não encontrado. Cadastre o paciente antes.")
            return

        data = input("Data do procedimento (YYYY-MM-DD): ")
        while not self.validar_data(data):
            print("⚠️ Data inválida. Use o formato YYYY-MM-DD.")
            data = input("Data do procedimento (YYYY-MM-DD): ")

        procedimento = input("Informe o nome do procedimento: ")

        self.db.execute(
            "INSERT INTO procedimentos (id_paciente, data, procedimento) VALUES (%s, %s, %s)",
            (paciente["id"], data, procedimento)
        )
        print("✅ Procedimento cadastrado com sucesso!")

    def listar(self):
        procedimentos = self.db.fetchall("""
            SELECT pr.id, p.nome, p.cpf, pr.data, pr.procedimento
            FROM procedimentos pr
            JOIN pacientes p ON pr.id_paciente = p.id
        """)
        if not procedimentos:
            print("⚠️ Nenhum procedimento encontrado.")
            return
        print("\nLista de Procedimentos:")
        print(tabulate(procedimentos, headers="keys", tablefmt="fancy_grid"))

    def editar(self):
        self.listar()
        try:
            id_procedimento = int(input("Digite o ID do procedimento que deseja editar: "))
        except ValueError:
            print("⚠️ ID inválido.")
            return

        proc = self.db.fetchone("SELECT * FROM procedimentos WHERE id = %s", (id_procedimento,))
        if not proc:
            print("⚠️ Procedimento não encontrado.")
            return

        nova_data = input(f"Nova data (Enter para manter {proc['data']}): ") or proc['data']
        while not self.validar_data(nova_data):
            print("⚠️ Data inválida. Use o formato YYYY-MM-DD.")
            nova_data = input(f"Nova data (Enter para manter {proc['data']}): ") or proc['data']

        novo_nome = input(f"Novo procedimento (Enter para manter {proc['procedimento']}): ") or proc['procedimento']

        self.db.execute(
            "UPDATE procedimentos SET data=%s, procedimento=%s WHERE id=%s",
            (nova_data, novo_nome, id_procedimento)
        )
        print("✅ Procedimento atualizado com sucesso!")

    def excluir(self):
        self.listar()
        try:
            id_procedimento = int(input("Digite o ID do procedimento que deseja excluir: "))
        except ValueError:
            print("⚠️ ID inválido.")
            return

        proc = self.db.fetchone("SELECT * FROM procedimentos WHERE id = %s", (id_procedimento,))
        if not proc:
            print("⚠️ Procedimento não encontrado.")
            return

        confirmar = input(f"Tem certeza que deseja excluir o procedimento de ID {id_procedimento}? (s/n): ").lower()
        if confirmar == "s":
            self.db.execute("DELETE FROM procedimentos WHERE id = %s", (id_procedimento,))
            print("✅ Procedimento excluído com sucesso!")
        else:
            print("❌ Exclusão cancelada.")
