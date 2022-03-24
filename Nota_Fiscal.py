from fastapi import FastAPI
import métodos
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

empresa = [
    {
    'id': 1,
    'nome_empresa': 'Rod_Raff',
    'cnpj': 14797440000126
    },
    {
    'id': 2,
    'nome_empresa': 'Máximo',
    'cnpj': 14803029000116
    }
]

nota_fiscal = [
    {
    'id': 1,
    'nome_empresa': 'Rod_Raff',
    'série': 'SG8R44',
    'número': 545257,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 2,
    'nome_empresa': 'Rod_Raff',
    'série': 'WV64D8',
    'número': 46635,
    'nome': 'Café Pilão tradicional 500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 3,
    'nome_empresa': 'Máximo',
    'série': 'SDI548',
    'número': 811628,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 4,
    'nome_empresa': 'Máximo',
    'série': 'D5SE2D',
    'número': 843821,
    'nome': 'Café_Pilão_tradicional_500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    }
]
app = FastAPI()

@app.get('/get-empresa/{nome_empresa}')
def get_empresa(nome_empresa: str):

    search = list(filter(lambda x: x['nome_empresa'] == nome_empresa, empresa))
    searchNF = métodos.cont_empresaNF(nota_fiscal, nome_empresa)
    if search == []:
        return {'Erro': 'O item não existe'}

    if searchNF == []:
        return {'Erro': 'O item não existe'}

    return {'Empresa': search,
            'Notas fiscais registradas': searchNF}

@app.get('/get-empresa/')
def get_empresas():
    return {'Empresas cadastradas:': empresa,
            'Notas fiscais Cadastradas': nota_fiscal}

@app.post('/post-empresa/')
def post_empresa(empresa_id: int, nome_empresa, cnpj):
    search = list(filter(lambda x: x['id'] == empresa_id, empresa))
    if search != []:
        return {'Erro': 'A empresa ja existe'}

    emp = {}
    emp['id'] = empresa_id
    emp['nome_empresa'] = nome_empresa
    emp['cnpj'] = cnpj
    empresa.append(emp)

@app.post('/post-nota_fiscal/')
def post_nota_fiscal(
    id_produto :int, nome_empresa,
    serie, numero, nome_produto,
    peso, cubagem, data):

    searchID = list(filter(lambda x: x['id'] == id_produto, nota_fiscal))
    search_empresa = list(filter(lambda x: x['nome_empresa'] == nome_empresa, empresa))
    print(search_empresa)

    if searchID != []:
        return {'Erro': 'Essa nota fiscal ja existe'}

    if nome_empresa not in search_empresa == []:
        return {'Erro': 'A empresa em que a nota fiscal está cadastrada não existe'}

    nf = {}
    nf['id'] = id_produto
    nf['nome_empresa'] = nome_empresa
    nf['série'] = serie
    nf['número'] = numero
    nf['nome'] = nome_produto
    nf['peso'] = peso
    nf['cubagem'] = cubagem
    nf['data'] = data
    nota_fiscal.append(nf)
