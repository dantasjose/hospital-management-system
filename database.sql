-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS hospital;
USE hospital;

-- =========================
-- Tabela de Pacientes
-- =========================
CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_nasc DATE NOT NULL,
    sexo ENUM('M', 'F') NOT NULL
);

-- =========================
-- Tabela de Consultas
-- =========================
CREATE TABLE IF NOT EXISTS consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    data DATE NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id) ON DELETE CASCADE
);

-- =========================
-- Tabela de Procedimentos
-- =========================
CREATE TABLE IF NOT EXISTS procedimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    data DATE NOT NULL,
    procedimento VARCHAR(150) NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id) ON DELETE CASCADE
);

-- =========================
-- Tabela de Logs
-- =========================
CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entidade VARCHAR(50) NOT NULL,       -- Paciente, Consulta, Procedimento
    acao VARCHAR(50) NOT NULL,           -- Cadastro, Edição, Exclusão
    detalhes TEXT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
