
from utils.db import Database
from tabulate import tabulate
from datetime import datetime


class Paciente:
    def __init__(self):
        self.db = Database()
    def cadastrar(self):
        nome = input("Informe nome e sobrenome do paciente: ")
        cpf = input("Informe o CPF (somente números): ")

        # Verificar se já existe CPF
        paciente_existente = self.db.fetchone("SELECT * FROM pacientes WHERE cpf = %s", (cpf,))
        if paciente_existente:
            print("⚠️ CPF já cadastrado!")
            return

          # Validação da data
        while True:
            data_nasc = input("Informe data de nascimento (YYYY-MM-DD): ")
            try:
                datetime.strptime(data_nasc, "%Y-%m-%d")
                break
            except ValueError:
                print("⚠️ Data inválida! Use o formato YYYY-MM-DD.")

        sexo = input("Informe o sexo (M/F): ").upper()
        while sexo not in ("M", "F"):
            print("⚠️ Sexo inválido. Digite apenas M ou F.")
            sexo = input("Informe o sexo (M/F): ").upper()

        # Inserir no banco
        self.db.execute(
            "INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
            (nome, cpf, data_nasc, sexo)
        )
        print("✅ Paciente cadastrado com sucesso!")

    def listar(self):
        pacientes = self.db.fetchall("SELECT * FROM pacientes")
        if not pacientes:
            print("⚠️ Nenhum paciente encontrado.")
            return
        print("\nLista de Pacientes:")
        print(tabulate(pacientes, headers="keys", tablefmt="fancy_grid"))

    def editar(self):
        cpf = input("Digite o CPF do paciente que deseja editar: ")
        paciente = self.db.fetchone("SELECT * FROM pacientes WHERE cpf = %s", (cpf,))
        if not paciente:
            print("⚠️ Paciente não encontrado.")
            return

        print(f"Editando paciente: {paciente['nome']} (CPF: {paciente['cpf']})")
        novo_nome = input(f"Novo nome (Enter para manter {paciente['nome']}): ") or paciente['nome']
        nova_data = input(f"Nova data nascimento (Enter para manter {paciente['data_nasc']}): ") or paciente['data_nasc']
        novo_sexo = input(f"Novo sexo (Enter para manter {paciente['sexo']}): ") or paciente['sexo']

        self.db.execute(
            "UPDATE pacientes SET nome=%s, data_nasc=%s, sexo=%s WHERE cpf=%s",
            (novo_nome, nova_data, novo_sexo, cpf)
        )
        print("✅ Paciente atualizado com sucesso!")

    def excluir(self):
        cpf = input("Digite o CPF do paciente que deseja excluir: ")
        paciente = self.db.fetchone("SELECT * FROM pacientes WHERE cpf = %s", (cpf,))
        if not paciente:
            print("⚠️ Paciente não encontrado.")
            return

        confirmar = input(f"Tem certeza que deseja excluir {paciente['nome']}? (s/n): ").lower()
        if confirmar == 's':
            self.db.execute("DELETE FROM pacientes WHERE cpf = %s", (cpf,))
            print("✅ Paciente removido com sucesso!")
        else:
            print("❌ Exclusão cancelada.")
        
    