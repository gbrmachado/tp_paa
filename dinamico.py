#!/usr/bin/env python
"""Arquivo contendo implementacao da selecao de atividades
    atraves de um metodo de programacao dinamica  """

import sys

from classes.atividade import Atividade
from classes.leitura import Leitura

NOME_ARQUIVO = sys.argv[1] # Obtem o nome do arquivo a ser lido
LISTA_ATIVIDADES = Leitura(NOME_ARQUIVO).get_atividades()
