from models.consulta import Consulta
from utils.db import Database

db = Database()
consulta_service = Consulta()

def test_cadastrar_consulta():
    db.execute("DELETE FROM pacientes WHERE cpf = %s", ("88888888888",))
    db.execute("INSERT INTO pacientes (nome, cpf, data_nasc, sexo) VALUES (%s, %s, %s, %s)",
               ("Paciente Consulta", "88888888888", "1995-05-05", "F"))
    paciente = db.fetchone("SELECT id FROM pacientes WHERE cpf = %s", ("88888888888",))
    paciente_id = list(paciente.values())[0]

    db.execute("INSERT INTO consultas (id_paciente, data, especialidade) VALUES (%s, %s, %s)",
               (paciente_id, "2025-10-10", "Cardiologia"))
    consulta = db.fetchone("SELECT * FROM consultas WHERE id_paciente = %s", (paciente_id,))
    assert consulta is not None

def test_editar_consulta():
    consulta = db.fetchone("SELECT * FROM consultas ORDER BY id DESC LIMIT 1")
    assert consulta is not None
    db.execute("UPDATE consultas SET especialidade=%s WHERE id=%s", ("Ortopedia", consulta["id"]))
    consulta_editada = db.fetchone("SELECT * FROM consultas WHERE id=%s", (consulta["id"],))
    assert consulta_editada["especialidade"] == "Ortopedia"

def test_excluir_consulta():
    consulta = db.fetchone("SELECT * FROM consultas ORDER BY id DESC LIMIT 1")
    assert consulta is not None
    db.execute("DELETE FROM consultas WHERE id=%s", (consulta["id"],))
    consulta_excluida = db.fetchone("SELECT * FROM consultas WHERE id=%s", (consulta["id"],))
    assert consulta_excluida is None
