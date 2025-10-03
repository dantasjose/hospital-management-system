from utils.db import Database
from models.paciente import Paciente
from tabulate import tabulate
from datetime import datetime

class Consulta:
    def __init__(self):
        self.db = Database()
        self.paciente_service = Paciente()

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

        data = input("Data da consulta (YYYY-MM-DD): ")
        while not self.validar_data(data):
            print("⚠️ Data inválida. Use o formato YYYY-MM-DD.")
            data = input("Data da consulta (YYYY-MM-DD): ")

        especialidade = input("Digite a especialidade: ")

        self.db.execute(
            "INSERT INTO consultas (id_paciente, data, especialidade) VALUES (%s, %s, %s)",
            (paciente["id"], data, especialidade)
        )
        print("✅ Consulta cadastrada com sucesso!")

    def listar(self):
        consultas = self.db.fetchall("""
            SELECT c.id, p.nome, p.cpf, c.data, c.especialidade
            FROM consultas c
            JOIN pacientes p ON c.id_paciente = p.id
        """)
        if not consultas:
            print("⚠️ Nenhuma consulta encontrada.")
            return
        print("\nLista de Consultas:")
        print(tabulate(consultas, headers="keys", tablefmt="fancy_grid"))

    def editar(self):
        self.listar()
        try:
            id_consulta = int(input("Digite o ID da consulta que deseja editar: "))
        except ValueError:
            print("⚠️ ID inválido.")
            return

        consulta = self.db.fetchone("SELECT * FROM consultas WHERE id = %s", (id_consulta,))
        if not consulta:
            print("⚠️ Consulta não encontrada.")
            return

        nova_data = input(f"Nova data (Enter para manter {consulta['data']}): ") or consulta['data']
        while not self.validar_data(nova_data):
            print("⚠️ Data inválida. Use o formato YYYY-MM-DD.")
            nova_data = input(f"Nova data (Enter para manter {consulta['data']}): ") or consulta['data']

        nova_especialidade = input(f"Nova especialidade (Enter para manter {consulta['especialidade']}): ") or consulta['especialidade']

        self.db.execute(
            "UPDATE consultas SET data=%s, especialidade=%s WHERE id=%s",
            (nova_data, nova_especialidade, id_consulta)
        )
        print("✅ Consulta atualizada com sucesso!")

    def excluir(self):
        self.listar()
        try:
            id_consulta = int(input("Digite o ID da consulta que deseja excluir: "))
        except ValueError:
            print("⚠️ ID inválido.")
            return

        consulta = self.db.fetchone("SELECT * FROM consultas WHERE id = %s", (id_consulta,))
        if not consulta:
            print("⚠️ Consulta não encontrada.")
            return

        confirmar = input(f"Tem certeza que deseja excluir a consulta de ID {id_consulta}? (s/n): ").lower()
        if confirmar == "s":
            self.db.execute("DELETE FROM consultas WHERE id = %s", (id_consulta,))
            print("✅ Consulta excluída com sucesso!")
        else:
            print("❌ Exclusão cancelada.")
