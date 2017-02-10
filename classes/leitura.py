""" Realiza a leitura de um arquivo e retorna uma lista de objetos Atividade """

from atividade import Atividade

class Leitura(object):
    """ Classe Leitura. Contem metodos para realizar leitura de arquivo texto
        converter para uma lista de objetos Atividade """
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.lista_atividades = []
        self.leitura_arquivo()

    def get_atividades(self):
        """ Retorna a lista de objetos atividade """
        return self.lista_atividades

    def leitura_arquivo(self):
        """ Realiza a leitura de um arquivo e conversao para lista de atividades """
        try:
            arq = open(self.nome_arquivo, 'r')
            lista_atv = arq.readlines()
            for i in lista_atv:
                aux_atividade = map(int, i.split("\n")[0].split(" "))
                self.lista_atividades.append(Atividade(aux_atividade[0], aux_atividade[1]))
            arq.close()

        except ValueError as error:
            print "Erro: " + repr(error)
            return

if __name__ == '__main__':
    LEITURA = Leitura("arquivos/teste.txt")
    for atividade in LEITURA.get_atividades():
        atividade.print_atividade()
