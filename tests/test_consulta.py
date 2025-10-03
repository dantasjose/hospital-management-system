import pytest
from models.consulta import Consulta
from utils.db import Database

db = Database()
consulta_service = Consulta()

def test_cadastrar_consulta():
    # Garantir que existe um paciente para vincular
    db.execute("DELETE FROM pacientes WHERE cpf = %s", ("88888888888",))
    db.execute(
        "INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
        ("Paciente Consulta", "88888888888", "1995-05-05", "F")
    )
    paciente = db.fetchone("SELECT id FROM pacientes WHERE cpf = %s", ("88888888888",))

    # Inserir consulta
    consulta_service.db.execute(
        "INSERT INTO consultas (id_paciente, data, especialidade) VALUES (%s, %s, %s)",
        (paciente["id"], "2025-10-10", "Cardiologia")
    )

    consulta = db.fetchone("SELECT * FROM consultas WHERE id_paciente = %s", (paciente["id"],))
    assert consulta is not None
    assert consulta["especialidade"] == "Cardiologia"
