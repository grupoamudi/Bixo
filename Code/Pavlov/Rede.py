import Camada

class Rede:
    #atributos:
    camadas = []
    
    #metodos:
    def __init__(self, numCamadas, matrizNeuronios):
        for i in range(numCamadas):
            self.camadas.append(Camada.Camada(matrizNeuronios[i]))
            
    def alimentarRede (self, entradas):
        entradasTemp = entradas
        for i in self.camadas:
            i.alimentarNeuronios(entradasTemp)
            entradasTemp = i.feedForward()
        
    def getResposta (self):
        ultimaCamada = self.camadas[-1]
        maiorSaida = 0
        for i in range(len(self.camadas[-1].neuronios)):
            if ultimaCamada.neuronios[i].axonio > maiorSaida:
                maiorSaida = ultimaCamada.neuronios[i].axonio
                indiceNeuronioMax = i

        return indiceNeuronioMax
        
            
