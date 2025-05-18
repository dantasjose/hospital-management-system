from datetime import datetime

CAMINHO_LOG = "dados/log.txt"

def registrar_log(acao):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {acao}\n"
    with open(CAMINHO_LOG, "a", encoding="utf-8") as f:
        f.write(linha)
