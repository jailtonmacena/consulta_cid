# consulta_cid
# Programa em Django para listar e buscar cids de acordo com sua categoria e descricao

# 1 - Entender o problema 

Uma das funcionalidades de uma aplicação que eu estava testando é buscar o CID pela categoria, subcategoria e pela descrição. Porém a aplicação não diferencia maiúsculas de minúsculas e também acentos então pensei porque não criar uma aplicação que resolva esse problema.

# 2 - Qual linguagem utilizar e framework 

Sei programar em Python e C# porém tenho mais familiaridade com Python e o framework Django então criarei uma aplicação web.

# 3 - Modelar a ideia da aplicação e entender como o Django gerencia isso com o modelo de MTV.
Definição os models, templates e view que vão ser utilizadas pela aplicação.
# 4 - Buscar a tabela de CIDs 

Sem elas não tem como eu criar a aplicação são as peças fundamentais então fiz pesquisa no google atrás do CID através do google dorks em site do governo site:data-sus.gov intext:CID então encontrei uma planilha com o que eu estava buscando vamos lá parti para o desenvolvimento

# 5 - Resolver o problema da consulta 

Sem essa funcionalidade minha aplicação seria igual a que eu já tinha acesso então busquei uma solução e 
me deparei com uma query feita em Django utilizando a funcionalidade do postgresql unaccent que retira todos os acentos da consulta ex: cólera = colera . O Django tem uma query interesse para não diferencia maiúsculas de minúsculas e pode ser combinado com o unaccent ficando assim objects.nome__unaccent__icontains()

# 6 - Preciso das funcionalidades
Agora preciso da funcionalidade de buscar o CID tanto pela sua categoria e subcategoria e também pela descrição. Para facilitar juntei as categorias com as subcategorias são bens parecidos.

# 7 - Mais funcionalidade
Estou conseguindo filtrar o que quero então vou listar os cids então criarei mais outra funcionalidade para listar todos os cids.

# 8 - Probelma para inserir muitos dados de uma vez no banco de dados
Pronto agora estou buscando e listando cids porém só adicionei uma pouca quantidade de forma manual só para testes mais tem 15000 cids no total e agora o que faço inserir isso tudo de forma manual é bem complicado. 

# 9 Buscando solução
Então busquei soluções para tal problema e me deparei que o banco postgresql também aceita importação de um tabela .csv, funcionou :)

## Problema com o banco de dados 
utilizando postgrsql
pip3 install psycopg2


sql prompt 

install CREATE EXTENSION unaccent;

