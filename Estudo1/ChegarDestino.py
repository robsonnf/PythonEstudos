#Imagine que existe uma pessoa nas coordenadas x=0 e y=0.
#Você recebe uma String no formato "NNSSEW" com as coordenadas de movimento e os parâmetros x e y com o destino da pessoa.
#Calcule se a pessoa chegou ou não no destino, retornando true ou false, seguindo a lógica:
#N= y+1
#S= y-1
#E= x+1
#W= x-1
#
#Exemplo:
#move="NNEES"
#x=2
#y=1
#
#Resultado: true

def chegou_no_destino(movimentos, x_destino, y_destino):
  """Verifica se uma pessoa, iniciando em (0,0) e seguindo os movimentos,
  chega ao destino (x_destino, y_destino).

  Args:
    movimentos: Uma string com os movimentos (N, S, E, W).
    x_destino: A coordenada x do destino.
    y_destino: A coordenada y do destino.

  Returns:
    True se a pessoa chegar ao destino, False caso contrário.
  """

  x, y = 0, 0  # Posição inicial

  for movimento in movimentos:
    if movimento == 'N':
      y += 1
    elif movimento == 'S':
      y -= 1
    elif movimento == 'E':
      x += 1
    elif movimento == 'W':
      x -= 1

  return x == x_destino and y == y_destino

# Exemplo de uso:
movimentos = "NNEES"
x_destino = 2
y_destino = 1

resultado = chegou_no_destino(movimentos, x_destino, y_destino)
print(resultado)  # Saída: True