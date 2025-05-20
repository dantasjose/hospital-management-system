import os
import pandas as pd
from utils.configs import Configuracoes
from models.paciente import Paciente
from datetime import datetime

class Consulta:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.paciente_service = Paciente()
        self.arquivo_csv = self.__configurations.file_consultas
        self.arquivo_id  = self.__configurations.file_ult_id_consulta

        if not os.path.exists(self.arquivo_csv) or os.path.getsize(self.arquivo_csv) == 0:
            df = pd.DataFrame(columns=['id', 'id_paciente', 'data', 'especialidade'])
            df.to_csv(self.arquivo_csv, index=False)

        if not os.path.exists(self.arquivo_id):
            with open(self.arquivo_id, 'w') as f:
                f.write('0')

    def validar_data(self, data_str):
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def gerar_novo_id(self):
        with open(self.arquivo_id, 'r') as f:
            ultimo_id = int(f.read())
        novo_id = ultimo_id + 1
        with open(self.arquivo_id, 'w') as f:
            f.write(str(novo_id))
        return novo_id

    def cadastrar(self):
        cpf = input("Digite o CPF do paciente: ")
        id_paciente = self.paciente_service.buscar(cpf) # Chama o método buscar na instância de Paciente
        if id_paciente == 0:
            print("Paciente não encontrado. Por favor, cadastre o paciente antes de agendar uma consulta.")
            return # Encerra a função cadastrar
        else:
            print(f"Paciente com ID: {id_paciente} Procedendo com o cadastro da consulta.")

            data = input('Data da consulta (dd/mm/aaaa): ')
            while not self.validar_data(data):
                print("Formato inválido. Tente novamente.")
                data = input('Data da consulta (dd/mm/aaaa): ')

            especialidade = input('Digite a especialidade: ')

            novo_id = self.gerar_novo_id()

            nova_linha = pd.DataFrame([{
                'id': novo_id,
                'id_paciente': id_paciente,
                'data': data,
                'especialidade': especialidade,
            }])

            df = pd.read_csv(self.arquivo_csv)
            df = pd.concat([df, nova_linha], ignore_index=True)
            df.to_csv(self.arquivo_csv, index=False)
            print(f'Consulta cadastrada com sucesso! ID: {novo_id}')

    def listar(self):
        df = pd.read_csv(self.arquivo_csv)

        if df.empty:
            print('Nenhuma consulta cadastrada.')
        else:
            #df = df.sort_values(by='id')
            #print(df[['id', 'paciente', 'data', 'medico']].to_string(index=False))
            print('\nLista de Consultas:')
            for index, row in df.iterrows():
                print(f"ID: {row['id']}, Paciente: {row['id_paciente']}, Data: {row['data']}, Especialidade: {row['especialidade']}")

    def editar(self):
        df = pd.read_csv(self.arquivo_csv)
        if df.empty:
            print("Nenhuma consulta para editar.")
            return

        print(df.to_string(index=False))
        try:
            id_editar = int(input("Digite o ID da consulta que deseja editar: "))
        except ValueError:
            print("ID inválido.")
            return

        if id_editar not in df['id'].values:
            print("ID não encontrado.")
            return

        linha = df[df['id'] == id_editar].iloc[0]

        nova_data = input(f"Nova data (Enter para manter '{linha['data']}'): ") or linha['data']
        while not self.validar_data(nova_data):
            print("Formato de data inválido. Tente novamente.")
            nova_data = input(f"Nova data (Enter para manter '{linha['data']}'): ") or linha['data']

        nova_especialidade = input(f"Nova especialidade (Enter para manter '{linha['especialidade']}'): ") or linha['especialidade']

        df.loc[df['id'] == id_editar, ['data', 'especialidade']] = [nova_data, nova_especialidade]
        df.to_csv(self.arquivo_csv, index=False)
        print("Consulta atualizada com sucesso.")

    def excluir(self):
        df = pd.read_csv(self.arquivo_csv)
        if df.empty:
            print("Nenhuma consulta para excluir.")
            return

        print(df.to_string(index=False))
        try:
            id_excluir = int(input("Digite o ID da consulta que deseja excluir: "))
        except ValueError:
            print("ID inválido.")
            return

        if id_excluir not in df['id'].values:
            print("ID não encontrado.")
            return

        confirm = input(f"Tem certeza que deseja excluir a consulta com ID {id_excluir}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Exclusão cancelada.")
            return

        df = df[df['id'] != id_excluir]
        df.to_csv(self.arquivo_csv, index=False)
        print(f"Consulta com ID {id_excluir} excluída com sucesso.")