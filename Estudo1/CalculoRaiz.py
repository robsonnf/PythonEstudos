import math

def calcular_raizes(a, b, c):
  """Calcula as raízes de uma equação do segundo grau.

  Args:
    a: Coeficiente quadrático.
    b: Coeficiente linear.
    c: Termo independente.

  Returns:
    Uma tupla com as raízes, caso existam, ou None caso contrário.
  """

  if a == 0:
    raise ValueError("O coeficiente 'a' não pode ser zero para uma equação do segundo grau.")

  delta = b**2 - 4*a*c

  if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2
  elif delta == 0:
    x = -b / (2*a)
    return x,
  else:
    return None

# Entrada de dados3
print("Digite os coeficientes da equação do segundo grau:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Chamada da função e exibição do resultado
try:
  raizes = calcular_raizes(a, b, c)
  if raizes:
    if len(raizes) == 1:
      print("A equação possui uma raiz real:", raizes[0])
    else:
      print("A equação possui duas raízes reais:", raizes)
  else:
    print("A equação não possui raízes reais.")
except ValueError as e:
  print(e)
