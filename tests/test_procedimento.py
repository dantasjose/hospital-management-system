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
    assert paciente is not None, "Paciente não foi inserido corretamente"

    paciente_id = list(paciente.values())[0]  # garante que pega o valor do id

    # Inserir procedimento
    db.execute(
        "INSERT INTO procedimentos (id_paciente, data, procedimento) VALUES (%s, %s, %s)",
        (paciente_id, "2025-11-11", "Exame de Sangue")
    )

    procedimento = db.fetchone("SELECT * FROM procedimentos WHERE id_paciente = %s", (paciente_id,))
    assert procedimento is not None, "Procedimento não foi inserido corretamente"
    assert procedimento["procedimento"] == "Exame de Sangue"
