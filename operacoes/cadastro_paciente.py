import pandas as pd
from tabulate import tabulate
import os

def cadastrar_paciente():
    nome_paciente = input('Informe nome e Sobrenome do Paciente: ')
    data_nascimento = input('Informe data de nascimento (dd/mm/aaaa): ')

    # Validação do CPF
    while True:
        cpf = input('Informe o CPF (somente números): ')
        if len(cpf) != 11 or not cpf.isdigit():
            print('Dados inválidos! Por favor, insira novamente.')
        else:
            dados = {
                'nome': [nome_paciente],
                'data_nascimento': [data_nascimento],
                'cpf': [cpf]
            }
            tabela_pacientes = pd.DataFrame(dados)

            # Exibição
            print('Cadastro realizado com sucesso!')
            print(tabulate(tabela_pacientes, headers='keys', tablefmt='grid'))

            # Salvar em CSV
            arquivo = 'pacientes.csv'
            if not os.path.isfile(arquivo):
                tabela_pacientes.to_csv(arquivo, index=False)
            else:
                tabela_pacientes.to_csv(arquivo, mode='a', index=False, header=False)
            break
