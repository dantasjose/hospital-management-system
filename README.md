# 🏥 Sistema de Gerenciamento Hospitalar

Este é um sistema simples de gerenciamento hospitalar, desenvolvido em **Python**, que agora utiliza **MySQL** para armazenamento dos dados.  

O projeto foi inicialmente feito com **arquivos CSV** como parte do projeto final da disciplina de **Algoritmos e Programação em Python** (Pós-Graduação em Ciência de Dados – Facens), e foi evoluído para integrar com banco de dados relacional em um cenário mais próximo de sistemas reais.

---

## ✅ Funcionalidades

- **Cadastro, listagem, edição e exclusão** de:
  - Pacientes
  - Consultas
  - Procedimentos
- **Validação de CPF** e **validação de datas**.
- **Relacionamento entre tabelas** (consultas e procedimentos vinculados ao paciente).
- **Sistema de logs** integrado ao banco de dados.
- **Interface interativa via terminal**.

---

## 🗂️ Estrutura do Projeto

hospital-management-system/
│
├── models/ # Camada de entidades e regras de negócio
│ ├── paciente.py # CRUD de pacientes
│ ├── consulta.py # CRUD de consultas
│ └── procedimento.py # CRUD de procedimentos
│
├── utils/ # Utilitários do sistema
│ ├── db.py # Conexão com MySQL
│ └── log.py # Gerenciamento de logs
│
├── tests/ # Testes automatizados com pytest
│ ├── test_paciente.py # Teste de cadastro de paciente
│ ├── test_consulta.py # Teste de cadastro de consulta
│ └── test_procedimento.py # Teste de cadastro de procedimento
│
├── database.sql # Script para criação do banco e tabelas
├── main.py # Ponto de entrada do sistema (menu principal)
├── README.md # Documentação do projeto
└── requirements.txt # Dependências do Python

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **MySQL 9.4+**
- **mysql-connector-python** — Conexão com banco
- **tabulate** — Formatação de tabelas no terminal
- **datetime** — Validação de datas
- **pytest** — Testes automatizados

---

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/dantasjose/hospital-management-system.git
cd hospital-management-system
2. Crie e ative o ambiente virtual
No Windows PowerShell:

bash
Copiar código
python -m venv venv
.\venv\Scripts\Activate.ps1
3. Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4. Configure o banco de dados MySQL
Certifique-se de que o MySQL está instalado e rodando.

Crie o banco hospital:

sql
Copiar código
CREATE DATABASE hospital;
USE hospital;
Execute o script SQL:

sql
Copiar código
SOURCE database.sql;
5. Execute o sistema
bash
Copiar código
python main.py
📁 Armazenamento de Dados
Todos os registros são armazenados no banco MySQL.

O banco possui as seguintes tabelas:

pacientes

consultas

procedimentos

logs

🧪 Testes Automatizados
O projeto utiliza pytest para validar funcionalidades básicas:

Cadastro de paciente

Cadastro de consulta

Cadastro de procedimento

Para rodar os testes:

bash
Copiar código
pytest -v
Exemplo de saída esperada:

arduino
Copiar código
tests/test_paciente.py::test_cadastrar_paciente PASSED
tests/test_consulta.py::test_cadastrar_consulta PASSED
tests/test_procedimento.py::test_cadastrar_procedimento PASSED
📌 Melhorias Futuras
Implementação de autenticação e controle de acesso.

Interface gráfica (GUI) ou versão Web.

Integração com APIs externas (ex.: convênios).

Relatórios estatísticos com pandas.

👥 Integrantes do Grupo Original
José Dantas

Waldir Pulzi Jr

Daniele Costa

Denis Borg

🎓 Contexto Acadêmico
Este projeto foi desenvolvido como requisito de avaliação para a disciplina de Algoritmos e Programação em Python no curso de Pós-Graduação em Ciência de Dados — Facens, e posteriormente evoluído para uso de MySQL em ambiente de aprendizado real.

📄 Licença
Este projeto é de uso acadêmico e está sob a licença MIT.

yaml
Copiar código

---

👉 Agora é só salvar esse conteúdo como `README.md`, depois fazer o commit e push:

```bash
git add README.md
git commit -m "docs: update README with MySQL integration and improved structure"
git push origin feature/mysql-integration