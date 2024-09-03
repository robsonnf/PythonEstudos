
#adicionando itens em listas:
print("Bem vindo à lista! Para adicionar um novo produto, informe o nome e o tipo.")
nome = input('Digite o nome do novo produto: ')
tipo = input('Informe o tipo do produto novo: ')
item_novo = f"{nome} ({tipo})"  # Cria uma string com o nome e o tipo do item

# suas listas
lista_pessoas = ['robson', 'ethiane', 'michelle']
lista_frutas = ['maçã', 'banana', 'abacaxi']
lista_feijoada = ['1 Kg de feijão preto',
'carne-seca',
'100 g de carne seca',
'orelha de porco',
'100 g de costelinha de porco',]
lista_docinhosDeFestas = ['brigadeiro','beijinho','cajuzinho']
lista_bebidas = ['coca-cola']


# Atualizando a listona (opcional, se você quiser uma lista única com todos os itens)
listona = lista_pessoas + lista_frutas + lista_feijoada + lista_docinhosDeFestas + lista_bebidas
print(listona[0])
# Criando a string formatada final
listonaf = f"""
Lista de pessoas: {', '.join(lista_pessoas)}
Lista de frutas: {', '.join(lista_frutas)}
Lista de feijoada: {', '.join(lista_feijoada)}
Lista de docinhos de festa: {', '.join(lista_docinhosDeFestas)}
Lista de bebidas: {', '.join(lista_bebidas)}
"""

# Imprimindo a string inicial
print(listonaf)

listonaf += f"""Adicionando nova lista de: Lista de Bebidas: {','.join(lista_bebidas)}
"""
print(listonaf)

# Adicionando o item novo à lista correta

produtos = {
    "pessoas": lista_pessoas,
    "frutas": lista_frutas,
    "feijoada": lista_feijoada,
    "docinhos de festa": lista_docinhosDeFestas,
    "bebidas": lista_bebidas
}

if 'bebida' in tipo.lower() and produtos['bebidas'] :
    lista_bebidas.append(item_novo)
elif 'fruta' in tipo.lower() and produtos['frutas'] :
    lista_frutas.append(item_novo)
elif 'ingrediente' in tipo.lower() and produtos['feijoada'] :
    lista_feijoada.append(item_novo)
elif 'docinho' in tipo.lower() and produtos['docinhos de festa'] :
    lista_docinhosDeFestas.append(item_novo)
elif 'pessoa' in tipo.lower() and produtos['pessoas'] :
    lista_pessoas.append(item_novo)
else:
    print("Tipo de item não reconhecido.")


listonaf = ""
for categoria, itens in produtos.items():
    listonaf += f"\n{categoria.capitalize()}: {', '.join(itens)}"

print(listonaf)
