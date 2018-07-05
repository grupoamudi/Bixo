import math
import random

class Neuronio:
    #atributos:
    mielina = []    #pesos
    dendritos = []  #entradas
    axonio = 0      #saida
    glia = 0       #passo de correcao

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

    def setGlia(self, erro):
        self.glia = erro * self.axonio * (1 - self.axonio)
    
    def corrigirNeuronio(self, erro):
        self.setGlia(erro)
        for index in range(len(self.mielina)):
            self.mielina[index] -= self.glia * self.dendritos[index]
    
    def produtoEscalar(self, vetorA, vetorB):
        resultado = 0
        for i in range(len(vetorB)):
            resultado += vetorA[i] * vetorB[i]
        return resultado
        
    def logistica(self, x):
        return (1/(1 + math.exp(-x)))
