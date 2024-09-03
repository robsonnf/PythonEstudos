import json
#Crie um dicionário vazio filmes = {}.
# Utilize o nome de um filme como chave.
# E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado.
# Preencha 5 filmes.

filmes = dict(filme="batman", vilão="coringa", ano=1989)
print(filmes)

# Criando um dicionário para armazenar as informações do novo filme
novo_filme = {}

# Obtendo informações do usuário
nome_filme = input("Nome do filme: ")
vilao_nome = input(f"Nome do vilão de {nome_filme}: ")
ano_lancamento = int(input(f"Ano de lançamento de {nome_filme}: "))

# Adicionando as informações ao dicionário
novo_filme["nome"] = nome_filme
novo_filme["vilao"] = vilao_nome
novo_filme["ano"] = ano_lancamento

# Imprimindo as informações do novo filme
print(f"O nome do filme é: {novo_filme['nome']}.")
print(f"O vilão é: {novo_filme['vilao']}.")
print(f"O ano de lançamento é: {novo_filme['ano']}.")

## Escrevendo os dados em um arquivo JSON
with open('filmes.json', 'a') as arquivo:
    json.dump(novo_filme, arquivo)
    arquivo.write('\n')  # Adiciona uma nova linha para separar cada filme

# Lendo os dados do arquivo JSON
with open('filmes.json', 'r') as arquivo:
    for linha in arquivo:
        filme = json.loads(linha)
        print(f"Nome do filme: {filme['nome']}")
        print(f"Vilão: {filme['vilao']}")
        print(f"Ano: {filme['ano']}")
        print("-" * 20)


import sqlite3

# Conectando ao banco de dados (criando se não existir)
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()

# Criando a tabela (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        ano INTEGER,
        diretor TEXT,
        genero TEXT,
        sinopse TEXT
    )
''')

# Inserindo um novo filme
cursor.execute('''
    INSERT INTO filmes (titulo, ano, diretor, genero, sinopse)
    VALUES (?, ?, ?, ?, ?)
''', ('O Poderoso Chefão', 1972, 'Francis Ford Coppola', 'Crime', 'A história de uma família mafiosa italiana'))

# Commitando as mudanças
conn.commit()

# Fechando a conexão
conn.close()

