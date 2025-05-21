from datetime import datetime
import os

def registrar_log(entidade: str, acao: str, identificador: str) -> None:
    """
    Registra ações do sistema em arquivo de log.
    Formato: [DATA HORA] AÇÃO - ENTIDADE - IDENTIFICADOR
    """
    try:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linha = f"[{data_hora}] {acao.upper()} - {entidade.upper()} - {identificador}\n"
        
        os.makedirs("dados", exist_ok=True)
        
        # Abre o arquivo forçando a escrita imediata (flush)
        with open("dados/log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)
            arquivo.flush()  # FORÇA A ESCRITA IMEDIATA
    except Exception:
        pass