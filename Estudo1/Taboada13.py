#taboada = {f"13x{i}": 13 * i for i in range(11)}
#
#for chave, valor in taboada.items():
#    print(chave, "=", valor)
#
#for valor in taboada.values():
#    if valor < 10:
#        print(valor)

# Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
numeros = []
for i in range(5):
    valor = float(input(f"Informe o {i+1}º valor: "))
    numeros.append(valor)

# Criando um dicionário com os valores (opcional, pode ser removido se não for necessário)
val = {}
for i, valor in enumerate(numeros):
    val[f"valor {i+1}"] = valor

# Ordenando uma cópia da lista para comparação
lista_ordenada = sorted(numeros)

# Verificando se a lista original é igual à lista ordenada
esta_ordenada = numeros == lista_ordenada

# Imprimindo os resultados
for chave, valor in val.items():
    print(chave, "=", valor)

print("Verificação, se esta ordenada de forma crescente:", esta_ordenada)



