#!/usr/bin/env python
"""Arquivo contendo implementacao da selecao de atividades
    atraves de um metodo de backtracking  """

import sys

from classes.atividade import Atividade
from classes.leitura import Leitura

NOME_ARQUIVO = sys.argv[1] # Obtem o nome do arquivo a ser lido
LISTA_ATIVIDADES = Leitura(NOME_ARQUIVO).get_atividades()

LISTA_ATIVIDADES.sort(key = lambda x: x.get_fim())  #ordena lista de atividades

NUM_JOBS = len(LISTA_ATIVIDADES)

i = NUM_JOBS - 1
lista_selecionadas = []
otimaVlr = 0
solucaoOtima = []

def backtracking(i):
    global otimaVlr
    global solucaoOtima
    global lista_selecionadas
    #   Retorna todas as atividades compativeis
    lista_compativeis = compativeis(i)
    if len(lista_compativeis) == 0:
        return LISTA_ATIVIDADES[i]
    for j in range(0, len(lista_compativeis)-1):
        lista_selecionadas.append( backtracking(lista_compativeis[j]))
    lista_selecionadas.append(LISTA_ATIVIDADES[i])
    if  otimaVlr < len(lista_selecionadas):
        otimaVlr = len(lista_selecionadas)
        solucaoOtima = lista_selecionadas
    lista_selecionadas =[]
    return LISTA_ATIVIDADES[i]

def compativeis(i):
    lista_compativeis = []
    for j in range(0,NUM_JOBS-1):
        if LISTA_ATIVIDADES[j].get_inicio() >= LISTA_ATIVIDADES[i].get_fim() and LISTA_ATIVIDADES[i] != LISTA_ATIVIDADES[j]:
            lista_compativeis.append(j)
    return lista_compativeis

for a in range(0,i):
    backtracking(a)

solucaoOtima.sort(key = lambda x: x.get_inicio() )
for atividade in solucaoOtima:
    atividade.print_atividade()
