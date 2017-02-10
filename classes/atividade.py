#!/usr/bin/env python
""" Arquivo contendo informacoes sobre a classe Atividade
    Classe que contem o inicio, e o fim de cada atividade"""

class Atividade(object):
    """ Classe atividade contendo informacoes sobre inicio e fim de atividade """
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def get_duracao(self):
        """ metodo que retorna a duracao de cada atividade """
        return self.fim - self.inicio

    def get_inicio(self):
        """ metodo que retorna o inicio de cada atividade """
        return self.inicio

    def get_fim(self):
        """ metodo que retorna o final de cada atividade """
        return self.fim

    def print_atividade(self):
        """ metodo que imprime uma atividade na tela """
        print "Inicio de atividade: " + str(self.get_inicio())
        print "Final de atividade: " + str(self.get_fim())
        print "Duracao de atividade: " + str(self.get_duracao())
        print "\n"
