import os

# Título
print("Cálculo do IMC")

# Entrada de dados
nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
altura_str = input("Digite sua altura em metros (ex: 1.75): ")

# Verifica se a altura contém vírgula
if ',' in altura_str:
    altura_str = altura_str.replace(',', '.')
    print("Sua altura foi ajustada para utilizar ponto como separador decimal.")

altura = float(altura_str)

# Cálculo do IMC
imc = peso / (altura ** 2)

# Saída formatada
print(f"""
Olá, {nome}!

Seus dados são:
* Idade: {idade} anos
* Peso: {peso:.2f} kg
* Altura: {altura:.2f} m
* IMC: {imc:.2f}

""")
# Interpretação do IMC (opcional)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso ideal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")