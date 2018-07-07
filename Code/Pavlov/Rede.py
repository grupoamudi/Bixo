import Camada

class Rede:
    #atributos:
    camadas = []
    entradas = 0

    #metodos:
    def __init__(self, numCamadas, matrizNeuronios, numeroDeEntradas):
        self.entradas = numeroDeEntradas
        for i in range(numCamadas):
            self.camadas.append(Camada.Camada(matrizNeuronios[i]))
    
    def alimentarRede (self, entradas):
        entradasTemp = entradas
        for camada in self.camadas:
            camada.alimentarNeuronios(entradasTemp)
            entradasTemp = camada.feedForward()
        
    def getIndiceResposta (self):
        ultimaCamada = self.camadas[-1]
        maiorSaida = 0
        for i in range(len(self.camadas[-1].neuronios)):
            if ultimaCamada.neuronios[i].axonio > maiorSaida:
                maiorSaida = ultimaCamada.neuronios[i].axonio
                indiceNeuronioMax = i
        return indiceNeuronioMax
    
    def aprender(self, alvos):
        #para a ultima camada:
        # alvos - saida ou saida - alvos?
        erro = [(-1)*(alvos[i] - self.camadas[-1].feedForward()[i]) for i in range(len(alvos))]
        self.camadas[-1].corrigirCamada(erro)
        #para as camadas ocultas e de entrada:
        erro = []
        # itera por todas as camadas da rede de tras para frente
        for c in range(len(self.camadas) - 2, -1, -1):
            # erro = Somatorio das glias * mielina que conecta o neuronio atual com o proximo
            # itera por todos os neuronios dessa camada
            for n in range (len(self.camadas[c].neuronios)):
                erroSing = 0
                # itera por cada neuronio da camada seguinte
                for m in range(len(self.camadas[c + 1].neuronios)):
                    erroSing += (self.camadas[c + 1].getGlias()[m] * self.camadas[c + 1].neuronios[m].mielina[n])
                erro.append(erroSing)
            self.camadas[c].corrigirCamada(erro)
            
