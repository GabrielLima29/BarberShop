import json
import os

CAMINHO_ARQUIVO = "data/clientes.json"

def carregar_clientes():
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump({}, f)
    with open(CAMINHO_ARQUIVO, "r") as f:
        return json.load(f)

def salvar_cliente(telefone, nome):
    clientes = carregar_clientes()
    clientes[telefone] = nome
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(clientes, f, indent=4)

def buscar_nome_por_telefone(telefone):
    clientes = carregar_clientes()
    return clientes.get(telefone)
