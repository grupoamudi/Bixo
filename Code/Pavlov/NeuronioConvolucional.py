#############################################
# Nome: NeuronioConvolucional.py            #
# Projeto: Projeto Pavlov                   #
# Autoria: Grupo aMuDi                      #
# Dependencia: random, math e Neuronio      #
# Status: Concluido                         #
#############################################
import math
import random
import Neuronio

# Classe NeuronioConvolucional: Representa um neoronio convolucional.
class NeuronioConvolucional:
    #Atributos:
    # 1. mielina: Representa a matriz de peso. O filtro deste neuronio.
    mielina = []
    # 2. dendritos: Representa a matri de leitura deste neuronio. Sera do
    ## tamanho do filtro.
    dendritos = []
    # 3. axonio: Representa a imagem de saida deste neuronio.
    axonio = []
    # 4. glia: Representa o gradiente descendente deste neuronio.
    glia = 0
    # 5. gliaAntiga: Representa o gradiente descendente antigo deste neuronio.
    gliaAntiga = 0

    #Metodos:
    # 1. __init__ :
    def __init__(self, larguraDaImagem, alturaDaImagem, stride, filtro):
        novaMielina = []
        for i in range(filtro):
            novaMielina.insert(i,[])
        for i in range(filtro):
            for j in range(filtro):
                novaMielina[i].insert(j,random.random())
        self.mielina = novaMielina

        percursoHorizontal = int(((larguraDaImagem - filtro)) / stride)
        percursoVertical = int(((alturaDaImagem - filtro)) / stride)

        for i in range(percursoVertical):
            self.axonio.insert(i,[])
            for j in range(percursoHorizontal):
                self.axonio[i].insert(j,0)

    def sinal(self, novaEntrada):
        for i in range (len(novaEntrada)):
            for j in range (len(novaEntrada[i])):
                self.dendritos[i][j] = novaEntada[i][j]

    def sinapse(self, stride, largura, altura):
        percursoHorizontal = (largura - len(mielina)) / stride
        percursoVertical = (altura - len(mielina)) / stride
        for i in range(percursoVertical):
            for j in range(percursoHorizontal):
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
