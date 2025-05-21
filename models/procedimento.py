import os
import pandas as pd
from utils.configs import Configuracoes
from models.paciente import Paciente
from datetime import datetime
from utils.log import registrar_log  # LINHA ADICIONADA

class Procedimento:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.paciente_service = Paciente()
        self.arquivo_csv = self.__configurations.file_procedimentos
        self.arquivo_id  = self.__configurations.file_ult_id_procedimento
        
        if not os.path.exists(self.arquivo_csv) or os.path.getsize(self.arquivo_csv) == 0:
            df = pd.DataFrame(columns=['id', 'id_paciente', 'data', 'procedimento'])
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
        id_paciente = self.paciente_service.buscar(cpf)
        if id_paciente == 0:
            print("Paciente não encontrado. Por favor, cadastre o paciente antes de agendar um procedimento.")
            return
        else:
            print(f"Paciente com ID: {id_paciente} Procedendo com o cadastro de procedimento.")

        data = input('Data do procedimento (dd/mm/aaaa): ')
        while not self.validar_data(data):
            print("Formato inválido. Tente novamente.")
            data = input('Data do procedimento (dd/mm/aaaa): ')
        
        procedimento = input('Procedimento: ')

        novo_id = self.gerar_novo_id()

        nova_linha = pd.DataFrame([{
            'id': novo_id,
            'id_paciente': id_paciente,
            'data': data,
            'procedimento': procedimento
        }])

        df = pd.read_csv(self.arquivo_csv)
        df = pd.concat([df, nova_linha], ignore_index=True)
        df.to_csv(self.arquivo_csv, index=False)
        print(f'Procedimento cadastrado com sucesso! ID: {novo_id}')
        
        # LINHA ADICIONADA
        registrar_log("Procedimento", "Cadastro", f"ID: {novo_id}, Paciente: {id_paciente}")

    def listar(self):
        df = pd.read_csv(self.arquivo_csv)
        if df.empty:
            print('Nenhum procedimento cadastrado.')
        else:
            for index, row in df.iterrows():
                print(f"ID: {row['id']}, ID do Paciente: {row['id_paciente']}, Data: {row['data']}, Procedimento: {row['procedimento']}")

    def editar(self):
        df = pd.read_csv(self.arquivo_csv)
        if df.empty:
            print("Nenhum procedimento para editar.")
            return

        print(df.to_string(index=False))
        try:
            id_editar = int(input("Digite o ID do procedimento que deseja editar: "))
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

        novo_procedimento = input(f"Novoprocedimento(Enter para manter '{linha['procedimento']}'): ") or linha['procedimento']

        df.loc[df['id'] == id_editar, ['data', 'procedimento']] = [nova_data, novo_procedimento]
        df.to_csv(self.arquivo_csv, index=False)
        print("Procedimento atualizado com sucesso.")
        
        # LINHA ADICIONADA
        registrar_log("Procedimento", "Edição", f"ID: {id_editar}")

    def excluir(self):
        df = pd.read_csv(self.arquivo_csv)
        if df.empty:
            print("Nenhum procedimento para excluir.")
            return

        print(df.to_string(index=False))
        try:
            id_excluir = int(input("Digite o ID do procedimento que deseja excluir: "))
        except ValueError:
            print("ID inválido.")
            return

        if id_excluir not in df['id'].values:
            print("ID não encontrado.")
            return

        confirm = input(f"Tem certeza que deseja excluir o procedimento com ID {id_excluir}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Exclusão cancelada.")
            return

        df = df[df['id'] != id_excluir]
        df.to_csv(self.arquivo_csv, index=False)
        print(f"Procedimento com ID {id_excluir} excluído com sucesso.")
        
        # LINHA ADICIONADA
        registrar_log("Procedimento", "Exclusão", f"ID: {id_excluir}")