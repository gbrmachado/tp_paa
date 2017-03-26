#!/usr/bin/env python
"""Arquivo contendo implementacao da selecao de atividades
    atraves de um metodo de backtracking  """

import sys
import copy
import time

start = time.time()

from classes.atividade import Atividade
from classes.leitura import Leitura

NOME_ARQUIVO = sys.argv[1] # Obtem o nome do arquivo a ser lido
LISTA_ATIVIDADES = Leitura(NOME_ARQUIVO).get_atividades()

LISTA_ATIVIDADES.sort(key = lambda x: x.get_fim())  #ordena lista de atividades

NUM_JOBS = len(LISTA_ATIVIDADES)

i = NUM_JOBS - 1
melhor = 0
solucaoOtima = []
lista_selecionadas = []

def compativeis(i):
    lista_compativeis = []
    for j in range( 0, NUM_JOBS ):
        if LISTA_ATIVIDADES[j].get_inicio() >= LISTA_ATIVIDADES[i].get_fim() and LISTA_ATIVIDADES[i] != LISTA_ATIVIDADES[j]:
            lista_compativeis.append(j)
    return lista_compativeis

def backtracking(i):
    global lista_selecionadas
    global melhor
    global solucaoOtima

    lista_selecionadas.append( LISTA_ATIVIDADES[i] )
    tamSelecionadas = len( lista_selecionadas )
    lista_compativeis = compativeis(i)

    if len( lista_compativeis )  == 0:
        if melhor <= tamSelecionadas:
            melhor = tamSelecionadas
            solucaoOtima = copy.copy( lista_selecionadas )
    else:
        for k in lista_compativeis:
            backtracking( k )

    #   Remove o ultimo elemento
    lista_selecionadas.pop()
    return

for a in range(0,NUM_JOBS):
    lista_selecionadas = []
    backtracking(a)


if (sys.argv[2] == "-p"):
    for i in solucaoOtima:
        i.print_atividade()
    print "Numero maximo de atividades: " + str(len(solucaoOtima))
if (sys.argv[2] == "-t"):
    print time.time() - start
