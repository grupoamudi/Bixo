import math
import random

class Neuronio:
    #atributos:
    mielina = []    #pesos
    dendritos = []  #entradas
    axonio = 0      #saida
    glia = []       #passo de correcao

    #metodos:
    def __init__(self, entradas):
        novaMielina = []
        for i in range(entradas):
            novaMielina.append(random.random())
        self.mielina = novaMielina
    
    def sinal(self, entrada):
        self.dendritos = entrada

    def sinapse(self):
        self.axonio = self.logistica(self.produtoEscalar(self.dendritos, self.mielina))

    def produtoEscalar(self, vetorA, vetorB):
        resultado = 0
        for i in range(len(vetorA)):
            resultado = resultado + vetorA[i] * vetorB[i]
        return resultado

    def logistica(self, x):
        return (1/(1 + math.exp(-x)))

    def derivLogistica(self, x):
        return self.logistica(x) * (1 - self.logistica(x))

    def setGlia(self, erro):
        pass
