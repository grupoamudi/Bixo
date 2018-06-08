import Camada

class Rede:
    #atributos:
    camadas = []
    
    #metodos:
    def __init__(self, numCamadas, matrizNeuronios):
        for i in range(numCamadas):
            self.camadas.append(Camada.Camada(matrizNeuronios[i]))
