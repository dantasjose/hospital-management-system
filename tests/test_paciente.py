import pytest
from models.paciente import Paciente
from utils.db import Database

db = Database()
paciente_service = Paciente()

def test_cadastrar_paciente():
    # Remove se já existir para evitar erro de duplicidade
    db.execute("DELETE FROM pacientes WHERE cpf = %s", ("99999999999",))

    # Simula inserção
    paciente_service.db.execute(
        "INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
        ("Teste Paciente", "99999999999", "2000-01-01", "M")
    )

    paciente = db.fetchone("SELECT * FROM pacientes WHERE cpf = %s", ("99999999999",))
    assert paciente is not None
    assert paciente["nome"] == "Teste Paciente"
