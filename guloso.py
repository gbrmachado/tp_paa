#!/usr/bin/env python
"""Arquivo contendo implementacao da selecao de atividades
    atraves de um metodo guloso """

import sys

from classes.atividade import Atividade
from classes.leitura import Leitura

NOME_ARQUIVO = sys.argv[1] # Obtem o nome do arquivo a ser lido
lista_atividades = Leitura(NOME_ARQUIVO).get_atividades() #gera lista de atividades a partir de leitura de arquivo

lista_atividades.sort(key = lambda x: x.get_fim())  #ordena lista de atividades

lista_selecionadas = [lista_atividades[0]]
ultima_selecionada = lista_atividades[0]

for atividade in lista_atividades[1:]:
    if atividade.get_inicio() >= ultima_selecionada.get_fim():
        lista_selecionadas.append(atividade)
        ultima_selecionada = atividade

for i in lista_selecionadas:
    i.print_atividade()
