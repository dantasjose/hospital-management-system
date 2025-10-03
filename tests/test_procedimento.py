import pytest
from models.procedimento import Procedimento
from utils.db import Database

db = Database()
procedimento_service = Procedimento()

def test_cadastrar_procedimento():
    # Garantir que existe um paciente para vincular
    db.execute("DELETE FROM pacientes WHERE cpf = %s", ("77777777777",))
    db.execute(
        "INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
        ("Paciente Procedimento", "77777777777", "1990-03-03", "M")
    )
    paciente = db.fetchone("SELECT id FROM pacientes WHERE cpf = %s", ("77777777777",))

    # Inserir procedimento
    procedimento_service.db.execute(
        "INSERT INTO procedimentos (id_paciente, data, procedimento) VALUES (%s, %s, %s)",
        (paciente["id"], "2025-11-11", "Exame de Sangue")
    )

    procedimento = db.fetchone("SELECT * FROM procedimentos WHERE id_paciente = %s", (paciente["id"],))
    assert procedimento is not None
    assert procedimento["procedimento"] == "Exame de Sangue"
