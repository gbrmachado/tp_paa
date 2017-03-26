#!/usr/bin/env python
"""Arquivo contendo implementacao da selecao de atividades
    atraves de um metodo de programacao dinamica  """

import sys
import time

start = time.time()

from classes.atividade import Atividade
from classes.leitura import Leitura

NOME_ARQUIVO = sys.argv[1] # Obtem o nome do arquivo a ser lido
LISTA_ATIVIDADES = Leitura(NOME_ARQUIVO).get_atividades()

LISTA_ATIVIDADES.sort(key = lambda x: x.get_fim())  #ordena lista de atividades

NUM_JOBS = len(LISTA_ATIVIDADES)

T = [1]*NUM_JOBS #Define uma lista contendo os pesos dos trabalhos. Todos iguais a um.

for j in range(1, NUM_JOBS): #Gera tabela contendo o numero de atividades maximo ate entao
    for i in xrange(j):
        if LISTA_ATIVIDADES[i].get_fim() <= LISTA_ATIVIDADES[j].get_inicio():
            T[j] = max(T[j], T[i] + 1)

i = NUM_JOBS - 1
while i >= 0:
    #calcula o mais proximo
    j = i-1
    while LISTA_ATIVIDADES[j].get_fim() > LISTA_ATIVIDADES[i].get_inicio() and j > 0:
        j = j - 1

    if 1 + T[j] > T[i-1]:
        if (sys.argv[2] == "-p"):
            LISTA_ATIVIDADES[i].print_atividade()
        i = j
    else:
        i = i-1

if (sys.argv[2] == "-p"):
    print "numero maximo de Tarefas: "+ str( max(T))

if (sys.argv[2] == "-t"):
    print time.time() - start
