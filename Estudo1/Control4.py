# Leia dois números e efetue a adição.
# Caso o valor somado seja maior que 20,
# este deverá ser apresentado somando-se a ele mais 8;
# caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

print('Olá, Bem Vindo! ')
a = float(input('Informe o primeiro valor: '))
b = float(input('Informe o segundo valor: '))

result = a + b

if result > 20:
    x = result + 8
    print('O resultado é',x)
elif result <= 20:
    y = result-5,
    print('O resultado é',y)
else:
    print("valores invalidos")




