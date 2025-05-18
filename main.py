import os
from utils.inicializar_arquivos import salvar_paciente
from models.paciente import Paciente
from models.consulta import Consulta

class Initialize():

    def show_menu(self): 
        print('\n')

        print(50 * '-')
        print('Bem-vindo ao Sistema do Hospital!')
        print(50 * '-')

        print('1 - Pacientes')
        print('2 - Consultas')
        print('3 - Procedimentos')
        print('4 - Listar logs')
        print('5 - Sair') 

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            print('\nOpção inválida!')

        return option

    def show_sub_menu(self, option):
        print('\n')

        print(50 * '-')

        if (option == '1'):  
            print('Pacientes:')
        elif (option == '2'):
            print('Consultas:')
        elif (option == '3'):
            print('Procedimentos:')

        print(50 * '-')

        print('1 - Cadastrar')
        print('2 - Editar')
        print('3 - Listar')
        print('4 - Excluir') 
        print('5 - Voltar menu principal') 

    def choose_sub_option(self):
        sub_option = input('\nEscolha uma das opções: ')

        if sub_option != '1' and sub_option != '2' and sub_option != '3' and sub_option != '4':
            print('\nOpção inválida!')

        return sub_option

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == "__main__":
    init = Initialize()
option = ''
pacientes = Paciente()
cons = Consulta()

while option != '5':
    init.show_menu()
    option = init.choose_option()

    if option == '1':  # Pacientes
        sub_option = ''
        while sub_option != '5':
            init.show_sub_menu(option)
            sub_option = init.choose_sub_option()

            if sub_option == '1':
                pacientes.cadastrar()
            elif sub_option == '2':
                pacientes.editar()
            elif sub_option == '3':
                pacientes.listar()  # se existir
            elif sub_option == '4':
                pacientes.excluir()

    elif option == '2':  # Consultas
        sub_option = ''
        while sub_option != '5':
            init.show_sub_menu(option)
            sub_option = init.choose_sub_option()

            if sub_option == '1':
                cons.cadastrar()
            elif sub_option == '2':
                cons.editar()
            elif sub_option == '3':
                cons.listar()
            elif sub_option == '4':
                cons.excluir()

    elif option == '3':  # Procedimentos (futuro)
        pass

    elif option == '4':
        init.to_go_out()