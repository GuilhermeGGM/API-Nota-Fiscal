nota_fiscal = [
    {
    'id': 10,
    'nome_empresa': 'Rod_Raff',
    'série': 'SG8R44',
    'número': 545257,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 11,
    'nome_empresa': 'Rod_Raff',
    'série': 'WV64D8',
    'número': 46635,
    'nome': 'Café Pilão tradicional 500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 20,
    'nome_empresa': 'Máximo',
    'série': 'SDI548',
    'número': 811628,
    'nome': 'Salgadinho_Lays_98g',
    'peso': '1.68Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    },
    {
    'id': 21,
    'nome_empresa': 'Máximo',
    'série': 'D5SE2D',
    'número': 843821,
    'nome': 'Café_Pilão_tradicional_500g',
    'peso': '6Kg',
    'cubagem': 300,
    'data': '10/03/2022'
    }
]

def cont_empresaNF(Nota_fiscal, empresa):
    cont = 0
    for emp in Nota_fiscal:
        if 'Rod_Raff' in emp.values() != False:
            cont += 1
    nf = cont
    return nf
