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

melhor = 0
listaMelhor = []
while i >= 0:
    #   Seleciona a atividade inicial da solucao
    lista_selecionadas = [LISTA_ATIVIDADES[i]]
    ultima_selecionada = LISTA_ATIVIDADES[i]

    for atividade in LISTA_ATIVIDADES[i+1:]:
        if atividade.get_inicio() >= ultima_selecionada.get_fim():
            lista_selecionadas.append(atividade)
            ultima_selecionada = atividade
    if  melhor < len(lista_selecionadas):
        melhor = len(lista_selecionadas)
        listaMelhor = lista_selecionadas

    i = i - 1
    lista_selecionadas = []

for atividade in listaMelhor:
    atividade.print_atividade()
