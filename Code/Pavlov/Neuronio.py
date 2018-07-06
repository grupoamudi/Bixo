import math
import random

#Classe Neuronio: Responsavel por representar um Neuronio na rede.
class Neuronio:
    #Atributos:
    # 1. Mielina: Representa os pesos. Cada indice esta associado
    #  a um neuronio da camada anterior. e.g.: o neuronio 2 da
    #  camada anterior se conecta a este neuronio pelo fio de
    #  mielina[2].
    mielina = []
    # 2. Dendritos: Representa as entradas. Cada indice esta
    #  associado a saida de cada neuronio da camada anterior.
    #  e.g.: O neuronio 0 da camada anterior tem a sua saida
    #  armazenada no dendritos[0] deste neuronio.
    dendritos = []
    # 3. Axonio: Representa a saida deste neuronio.
    axonio = 0
    # 4. Glia: Representa o Gradiente Descendente, o passo de
    #  correcao deste neuronio.
    glia = 0
    # 5. GliaResidual: Representa a glia antiga. Usada para
    #  treino com momentum.
    gliaResidual = 1

    #Metodos:
    # 1. Construtor: Ao criar um neuronio, eh preciso especificar
    #  um int de quantas entradas ele tem.
    #  Ele então ira atualizar o vetor de mielina com valores
    #  aleatorios. O vetor tera o tamanho especificado pela entrada
    def __init__(self, entradas):
        novaMielina = []
        for i in range(entradas):
            novaMielina.append(random.random())
        self.mielina = novaMielina

    # 2. Sinal: Atualiza as entradas deste neuronio
    def sinal(self, entrada):
        self.dendritos = entrada

    # 3. Sinapse: Atualiza o valor de sua saida como sendo
    #  o resultado da funcao de ativacao.
    def sinapse(self):
        self.axonio = self.logistica(self.produtoEscalar(self.dendritos, self.mielina))

    # 4. SetGlia: Determina o invariante do vetor gradiente
    #  descendente.
    def setGlia(self, erro):
        self.glia = erro * self.derivLogistica(self.produtoEscalar(self.mielina, self.dendritos))

    # 5. ProdutoEscalar: Retorna o produto escalar do vetor A
    #  com o vetor B.
    def produtoEscalar(self, vetorA, vetorB):
        resultado = 0
        for i in range(len(vetorB)):
            resultado += vetorA[i] * vetorB[i]
        return resultado

    # 6. Logistica: Implementacao da funcao logistica (usada
    #  como funcao de ativacao).
    def logistica(self, x):
        return (1/(1 + math.exp(-x)))

    # 7. DerivLogistica: Implementacao da funcao derivada da
    #  logistica. Usada para Backpropagation.
    def derivLogistica (self, x):
        return self.logistica(x) * (1 - self.logistica(x))

    # 8. Corrigir Neuronio: Corrige as mielinas do neuronio.
    def corrigirNeuronio(self, erro):
        self.setGlia(erro)
        for i in range(len(self.mielina)):
            self.mielina[index] -= self.glia * self.dendritos[index]
