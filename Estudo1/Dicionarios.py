# Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor.
from collections.abc import dict_items
from contextlib import nullcontext

pessoas = {"robson": "branco", "tallita": "cinza", "rita": "preta", "marco":"nu", "guilherme" : "vermelho"}

print(pessoas)
# Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor uma lista com as aulas que você tem nesse dia
# (sábado e domingo recebem listas vazias, ou você tem aula?).

semana ={"segunda":"aula","terça":"aula2","quarta":"aula3","quinta":"aula4","sexta":"aula5","sabado":"","domingo":""}

print(semana)
#