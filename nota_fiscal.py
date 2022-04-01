from fastapi import FastAPI
import metodos
from typing import Optional
from pydantic import BaseModel
from utilis import nota_fiscal, empresa

app = FastAPI()

class item(BaseModel):
    id: int
    nome_empresa: str
    serie: str
    numero: str
    nome: str
    peso: str
    cubagem: int
    data: str
class UpdateItem(BaseModel):
    id: Optional[int] = None
    nome_empresa: Optional[str] = None
    serie: Optional[str] = None
    numero: Optional[str] = None
    nome: Optional[str] = None
    peso: Optional[str] = None
    cubagem: Optional[int] = None
    data: Optional[str] = None

@app.get('/get-empresa/{nome_empresa}')
def get_empresa(nome_empresa: str):

    search = list(filter(lambda x: x['nome_empresa'] == nome_empresa, empresa))
    searchNF = metodos.cont_empresaNF(nota_fiscal, nome_empresa)
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

@app.post('/post-empresa/', status_code= 201)
def post_empresa(empresa_id: int, nome_empresa, cnpj):
    search = list(filter(lambda x: x['id'] == empresa_id, empresa))
    if search != []:
        return {'Erro': 'A empresa ja existe'}

    emp = {}
    emp['id'] = empresa_id
    emp['nome_empresa'] = nome_empresa
    emp['cnpj'] = cnpj
    empresa.append(emp)

@app.post('/post-nota_fiscal/', status_code=201)
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

@app.put('/update/{nota_fiscal_id}')
def updateNF(item_id: int, item:UpdateItem):
    search = list(filter(lambda x: x['id'] == item_id, nota_fiscal))

    if search == []:
        return {'Erro': 'O intem não existe ou ja foi deletado'}

    if item.id is not None:
        search[0]['id'] = item.id
    if item.nome_empresa is not None:
        search[0]['nome_empresa'] = item.nome_empresa
    if item.serie is not None:
        search[0]['serie'] = item.serie
    if item.numero is not None:
        search[0]['numero'] = item.numero
    if item.nome is not None:
        search[0]['nome'] = item.nome
    if item.peso is not None:
        search[0]['peso'] = item.peso
    if item.cubagem is not None:
        search[0]['cubagem'] = item.nome
    if item.data is not None:
        search[0]['data'] = item.nome

    return search

@app.delete('/delete-item/{id_nota_fiscal}')
def deleteNF(nf_id: int):
    search = list(filter(lambda x:x['id'] == nf_id, nota_fiscal))

    if search == []:
        return {'Erro': 'O item não existe ou ja foi deletado'}

    for i in range(len(nota_fiscal)):
        if nota_fiscal[i]['id'] == nf_id:
            del nota_fiscal[i]
            break
    return {'O item foi deletado com sucesso'}
