import Neuronio

class Camada:
    #atributos:
    neuronios = [] #neuronios contidos na camada
    saidasDaCamada = [] #contem a saida de todos os neuronios da camada

    #metodos:
    def __init__(self, neuroniosInput):
        self.neuronios = neuroniosInput

    def getSaidas (self):
        novasSaidas = []
        for i in self.neuronios:
            novasSaidas.append(i.axonio)

        self.saidasDaCamada = novasSaidas
        
