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
        for camada in self.camadas:
            camada.alimentarNeuronios(entradasTemp)
            entradasTemp = camada.feedForward()
        
    def getResposta (self):
        ultimaCamada = self.camadas[-1]
        maiorSaida = 0
        for i in range(len(self.camadas[-1].neuronios)):
            if ultimaCamada.neuronios[i].axonio > maiorSaida:
                maiorSaida = ultimaCamada.neuronios[i].axonio
                indiceNeuronioMax = i
        return indiceNeuronioMax
    
    def aprender(self, alvos):
        #para a ultima camada:
        erro = [alvos[i] - self.camadas[-1].feedForward()[i] for i in range(len(alvos))]
        self.camadas[-1].corrigirCamada(erro)
        #para as camadas ocultas e de entrada:
        erro = []
        for c in range(len(self.camadas) - 2, -1, -1):
            erro = [sum(neuronio.glia for neuronio in self.camadas[c].neuronios)]
            self.camadas[c].corrigirCamada(erro)
            
