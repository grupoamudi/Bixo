#############################################
# Nome: NeuronioConvolucional.py            #
# Projeto: Projeto Pavlov                   #
# Autoria: Grupo aMuDi                      #
# Dependencia: Neuronio.py                  #
# Status: Concluido                         #
#############################################

import math
import random
import Neuronio

class NeuronioConvolucional:
    # atributos:
    mielina = [] # pesos
    imagem = [] # imagem carregada
    dendritos = [] # entradas
    axonio = [] # saida
    glia = 0 # passo de correção
    gliaAntiga = 0 # passo de correção por momentum
    larguraDaImagem = 0 # largura da imagem
    alturaDaImagem = 0 # altura da imagem
    stride = 0 # passos com os quais se atualizam as entradas dos dendritos.
    filtro = 0 # dimensao do filtro

    # metodos:
    #   __init__: e preciso especificar a largura e a altura da imagem.
    #    stride e filtro sao características intrínsecas ao neuronio de convolucao.
    #    stride representa o passo de leitura do filtro sobre a imagem.
    #    filtro representa a dimensao do filtro que este neuronio representa.
    def __init__(self, larguraDaImagem, alturaDaImagem, stride, filtro):
        # Inicializacao de pesos aleatorios para a matriz do filtro deste neuronio.
        novaMielina = []
        for i in range(filtro):
            novaMielina.insert(i,[])
            self.dendritos.insert(i,[])
        for i in range(filtro):
            for j in range(filtro):
                novaMielina[i].insert(j,random.random())
                self.dendritos.insert(j,0)
        self.mielina = novaMielina
        # Descricao finalizada.

        # Atualiza parametros do neuronio.
        self.larguraDaImagem = larguraDaImagem
        self.alturaDaImagem = alturaDaImagem
        self.stride = stride
        self.filtro = filtro
        # Descricao finalizada

        # Define o tamanho da matriz de saida para o neuronio.
        percursoHorizontal = int(((larguraDaImagem - filtro)) / stride)
        percursoVertical = int(((alturaDaImagem - filtro)) / stride)

        for i in range(percursoVertical):
            self.axonio.insert(i,[])
            for j in range(percursoHorizontal):
                self.axonio[i].insert(j,0)
        # Descricao finalizada.

    #   sinal: e preciso especificar a imagem (uma matriz).
    #    esta funcao carrega a imagem para o neuronio
    def sinal(self, novaEntrada):
        print (novaEntrada)
        self.imagem = novaEntrada
    #   Descricao finalizada

    #   percorre: e preciso especificar em qual secao da imagem se deseja analizar
    #       esta funcao atualiza o valor da entrada para uma secao da imagem.
    def percorre(self, i, j):
        for a in range(self.filtro):
            for b in range(self.filtro):
                self.dendritos[a][b] = self.imagem[a + i][b + j]
    #   Descricao finalizada

    def sinapse(self):
        percursoHorizontal = int((self.larguraDaImagem - len(self.mielina)) / self.stride)
        percursoVertical = int((self.alturaDaImagem - len(self.mielina)) / self.stride)
        for i in range(percursoVertical):
            for j in range(percursoHorizontal):
                self.percorre(i,j)
                self.axonio[i][j] = self.logistica(self.produtoEscalar(self.dendritos, self.mielina))

    def produtoEscalar(self, matrizA, matrizB):
        resposta = 0
        for i in range(len(matrizB)):
            for j in range(len(matrizB[i])):
                resposta += matrizA[i][j] * matrizB[i][j]
        return resposta

    def logistica(self, x):
        return (1/(1 + math.exp(-x)))

    # Funções de Aprendizado
    def setGlia(self, erro):
        self.glia = erro * self.axonio * (1 - self.axonio)

    def corrigirNeuronio(self, erro):
        self.setGlia(erro)
        for index in range(len(self.dendritos)):
            self.mielina[index] -= self.glia * self.dendrito[index]

    # métodos de debugging
    def printMielina(self):
        for i in range (len(self.mielina)):
            print("Coluna {}".format(i))
            for j in range (len(self.mielina[i])):
                print ("\t Linha {} : {}".format(j,self.mielina[i][j]))

    def printAxonio(self):
        for i in range (len(self.axonio)):
            print("Coluna {}".format(i))
            for j in range (len(self.axonio[i])):
                print ("\t Linha {} : {}".format(j,self.axonio[i][j]))

    def testarProdutoEscalar(self):
        a = [[1,1,1],[1,1,1],[1,1,1]]
        b = [[3,2,1],[6,5,4],[9,8,7]]
        print (self.produtoEscalar(a,b))

    def printTamanhoMielina(self):
        print (len(self.mielina) * len(self.mielina[0]))

    def printTamanhoSaida(self):
        print (len(self.axonio) * len(self.axonio[0]))

    def printDendritos(self):
        for i in range (len(self.dendritos)):
            print("Coluna {}".format(i))
            for j in range (len(self.dendritos[i])):
                print ("\t Linha {} : {}".format(j,self.dendritos[i][j]))
