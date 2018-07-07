import Neuronio

class Camada:
    #atributos:
    neuronios = [] #neuronios contidos na camada
    saidasDaCamada = [] #contem a saida de todos os neuronios da camada

    #metodos:
    def __init__(self, neuroniosInput):
        self.neuronios = neuroniosInput
        self.saidasDaCamada = [0 for i in range(len(self.neuronios))]

    def updateSaidas (self):
        for i in range(len(self.neuronios)):
            self.saidasDaCamada[i] = self.neuronios[i].axonio
        
    def alimentarNeuronios (self, entradas):
        for neuronio in self.neuronios:
            neuronio.dendritos = entradas
            neuronio.sinapse()

    def feedForward (self):
        self.updateSaidas()
        return self.saidasDaCamada
    
    def corrigirCamada(self, erro):
        for n in range(len(self.neuronios)):
            self.neuronios[n].corrigirNeuronio(erro[n])

    def getGlias(self):
        glias = []
        for i in self.neuronios:
            glias.append(i.glia)
        return glias
