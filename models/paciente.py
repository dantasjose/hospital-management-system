import os
from tabulate import tabulate
import pandas as pd
from utils.configs import Configuracoes

class Paciente:
    def __init__(self):
        self.__configurations = Configuracoes()
        self.arquivo_csv = self.__configurations.file_pacientes
        self.arquivo_id  = self.__configurations.file_ult_id_paciente
        
        # Criar arquivo CSV se não existir
        if not os.path.exists(self.arquivo_csv):
            df = pd.DataFrame(columns=['id', 'nome', 'cpf', 'data_nasc', 'sexo'])
            df.to_csv(self.arquivo_csv, index=False)
        
        # Criar arquivo de ID se não existir ou estiver vazio
        if not os.path.exists(self.arquivo_id) or os.path.getsize(self.arquivo_id) == 0:
            with open(self.arquivo_id, 'w') as f:
                f.write('0')

    def gerar_novo_id(self):
        with open(self.arquivo_id, 'r') as f:
            conteudo = f.read().strip()
            ultimo_id = int(conteudo) if conteudo else 0
        
        novo_id = ultimo_id + 1
        with open(self.arquivo_id, 'w') as f:
            f.write(str(novo_id))
        return str(novo_id)

    def cadastrar(self):
        df = pd.read_csv(self.arquivo_csv)
        nome = input('Informe nome e sobrenome do paciente: ')
        cpf = input('Informe o cpf (somente números): ')

        if cpf in df['cpf'].astype(str).values:
            print('CPF já cadastrado!')
            return

        while len(cpf) != 11 or not cpf.isdigit():
                print('CPF inválido! Deve conter exatamento 11 dígitos numéricos.')
                cpf = input('Informe novamente o CPF (somente números): ')
           
        data_nasc = input('Informe a data de nascimento: ')
        sexo = input('Informe o sexo: ')

        novo_id = self.gerar_novo_id()
        novo_paciente = pd.DataFrame([[str(novo_id), str(nome), str(cpf), str(data_nasc), str(sexo)]], 
                                    columns=['id', 'nome', 'cpf', 'data_nasc', 'sexo'], dtype=str)
        
        # Adiciona ao arquivo existente
        novo_paciente.to_csv(self.arquivo_csv, mode='a', header=False, index=False)
        print(f'Paciente cadastrado com sucesso! ID: {novo_id}')
        print(tabulate(novo_paciente, headers='keys', tablefmt='grid', showindex=False))

    def listar(self):
        df = pd.read_csv(self.arquivo_csv, dtype={'id': str})
        
        if df.empty:
            print('Nenhum paciente cadastrado.')
        else:
            print('\nLista de Pacientes:')
            df_formatado = df[['id', 'nome', 'cpf', 'data_nasc']]
            print(tabulate(df_formatado, headers='keys', tablefmt='grid', showindex=False))

    def excluir(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente para excluir.')
            return

        self.listar()
        id_excluir = input('Digite o ID do paciente que deseja excluir: ').strip()    
        df['id'] = df['id'].astype(str)  # Converter para string para evitar problemas de type

        if id_excluir not in df['id'].values:
            print('ID não encontrado')
            return
        
        df = df[df['id'] != id_excluir]
        df.to_csv(self.arquivo_csv, index=False)
        print(f'Paciente com ID {id_excluir} removido com sucesso.')
        self.excluir_registros_relacionados(id_excluir)

    def excluir_registros_relacionados(self, id_paciente):
        caminho_consulta = 'dados/consulta.csv'
        if os.path.exists(caminho_consulta):
            df = pd.read_csv(caminho_consulta, dtype={'id_paciente': str})

            if 'id_paciente' not in df.columns:
                print('A coluna "id_paciente" não existe no arquivo de consultas.')
                return

            df['id_paciente'] = df['id_paciente'].astype(str)
            id_paciente = str(id_paciente)

            original = len(df)
            df = df[df['id_paciente'] != id_paciente]
            df.to_csv(caminho_consulta, index=False)
            removidos = original - len(df)
            if removidos > 0:
                print(f'{removidos} consulta(s) relacionada(s) ao paciente ID {id_paciente} foram excluída(s).')

    def editar(self):
        df = pd.read_csv(self.arquivo_csv)
        
        if df.empty:
            print('Nenhum paciente cadastrado para editar.')
            return
       
        id_editar = input('Digite o ID do paciente que deseja editar: ').strip()
        
        # Converter para string para evitar problemas de tipo
        df['id'] = df['id'].astype(str)
        
        if id_editar not in df['id'].values:
            print('ID não encontrado.')
            return
            
        paciente = df[df['id'] == id_editar].iloc[0]
        print("\nDados atuais do paciente:")
        print(f"1. Nome: {paciente['nome']}")
        print(f"2. CPF: {paciente['cpf']}")
        print(f"3. Data de Nascimento: {paciente['data_nasc']}")
        print(f"4. Sexo: {paciente['sexo']}")
        
        campo = input("\nDigite o número do campo que deseja editar (1-4): ")
        novo_valor = input("Digite o novo valor: ")
        
        if campo == '1':
            df.loc[df['id'] == id_editar, 'nome'] = novo_valor
        elif campo == '2':
            df.loc[df['id'] == id_editar, 'cpf'] = novo_valor
        elif campo == '3':
            df.loc[df['id'] == id_editar, 'data_nasc'] = novo_valor
        elif campo == '4':
            df.loc[df['id'] == id_editar, 'sexo'] = novo_valor
        else:
            print("Opção inválida.")
            return
            
        df.to_csv(self.arquivo_csv, index=False)
        print("Paciente atualizado com sucesso!")