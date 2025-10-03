from models.procedimento import Procedimento
from utils.db import Database

db = Database()
procedimento_service = Procedimento()

def test_cadastrar_procedimento():
    db.execute("DELETE FROM pacientes WHERE cpf = %s", ("77777777777",))
    db.execute("INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
               ("Paciente Procedimento", "77777777777", "1990-03-03", "M"))
    paciente = db.fetchone("SELECT id FROM pacientes WHERE cpf = %s", ("77777777777",))
    paciente_id = list(paciente.values())[0]

    db.execute("INSERT INTO procedimentos (id_paciente, data, procedimento) VALUES (%s, %s, %s)",
               (paciente_id, "2025-11-11", "Exame de Sangue"))
    procedimento = db.fetchone("SELECT * FROM procedimentos WHERE id_paciente = %s", (paciente_id,))
    assert procedimento is not None

def test_editar_procedimento():
    procedimento = db.fetchone("SELECT * FROM procedimentos ORDER BY id DESC LIMIT 1")
    assert procedimento is not None
    db.execute("UPDATE procedimentos SET procedimento=%s WHERE id=%s", ("Raio-X", procedimento["id"]))
    procedimento_editado = db.fetchone("SELECT * FROM procedimentos WHERE id=%s", (procedimento["id"],))
    assert procedimento_editado["procedimento"] == "Raio-X"

def test_excluir_procedimento():
    procedimento = db.fetchone("SELECT * FROM procedimentos ORDER BY id DESC LIMIT 1")
    assert procedimento is not None
    db.execute("DELETE FROM procedimentos WHERE id=%s", (procedimento["id"],))
    procedimento_excluido = db.fetchone("SELECT * FROM procedimentos WHERE id=%s", (procedimento["id"],))
    assert procedimento_excluido is None
