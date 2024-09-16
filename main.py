import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from pred import model

app = FastAPI()


class PrevisaoInput(BaseModel):
    imp_transp_pub: float
    imp_infra: float
    nome: str


regioes = {}

@app.post("/regiao/")
def criar_regiao(input: PrevisaoInput):
    regioes[input.nome] = {
        "imp_transp_pub": input.imp_transp_pub,
        "imp_infra": input.imp_infra
    }
    return {"mensagem": "Região adicionada com sucesso!"}

@app.get("/previsao/{nome}")
def prever_valor(nome: str):
    if nome not in regioes:
        return {"erro": "Região não encontrada!"}
    dados_regiao = regioes[nome]
    X_input = np.array([[dados_regiao["imp_transp_pub"], dados_regiao["imp_infra"]]])
    previsao_valor = model.predict(X_input)[0]
    
    return {"regiao": nome, "valor_previsao": previsao_valor}