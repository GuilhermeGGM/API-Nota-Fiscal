# API de administração de nota fiscal
Essa api foi construída para fins de aprendizado.

Ela simula a comunicação com um banco de dados referente a administração de notas fiscais.

# Como rodar a aplicação
Clone o projeto:
>git@github.com:GuilhermeGGM/API-Nota-Fiscal.git

>Versão utilizada do Python: 3.6

No terminal, ecreva o seguinte código para criar a Virtualenv:
>Instalar: pip install virtualenv
>Criar virtualenv: virtualenv venv
  
>Ativar: source venv/bin/activate
  
>Desativar: deactivate

Instale as dependências:
>pip install -r requirements.txt

Para iniciar a aplicação:
>uvicorn nota_Fiscal:app --reload

>Cole o link que aparecer no terminal no seu 
>navegador e em seguida adiocione um "/docs".

>Você vai ser direcionado para esse endereço:
>https://github.com/GuilhermeGGM/API-Nota-Fiscal/issues/2#issue-1189893562

# Próximos passos
>Melhorar o PUT

>Adicionar um validador de cnpj
