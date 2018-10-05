import Camada

#Classe Rede representa a estrutura de dado de uma Rede Neural.
class Rede:
    #Atributos:
    # 1. Camadas: Vetor que guarda os objetos da classe Camada que pertencem a rede.
    #  Do menor para o maior indice, segue a ordem das camadas desde a entrada até a saida.
    camadas = []
    # 2. Entradas: Valor que indica o numero de entradas que esta rede espera receber
    entradas = 0

    #Metodos:
    # 1. Construtor: Define o numero de entradas que essa rede espera receber e cria/atualiza
    #  os neuronios que pertencem a cada camada.
    def __init__(self, numCamadas, matrizNeuronios, numeroDeEntradas):
        self.entradas = numeroDeEntradas
        for i in range(numCamadas):
            self.camadas.append(Camada.Camada(matrizNeuronios[i]))

    # 2. AlimentarRede: Esta funcao alimenta as entradas para a rede e propaga as saidas
    #  de cada camada para a camada seguinte ate chegar a ultima camada.
    def alimentarRede (self, entradas):
        entradasTemp = entradas
        for camada in self.camadas:
            camada.alimentarNeuronios(entradasTemp)
            entradasTemp = camada.feedForward()

    # 3. GetIndiceResposta: Retorna o indice do neuronio na ultima camada
    #  que retorna o maior valor de saída
    def getIndiceResposta (self):
        ultimaCamada = self.camadas[-1]
        maiorSaida = 0
        for i in range(len(self.camadas[-1].neuronios)):
            if ultimaCamada.neuronios[i].axonio > maiorSaida:
                maiorSaida = ultimaCamada.neuronios[i].axonio
                indiceNeuronioMax = i
        return indiceNeuronioMax

    # 4. Aprender: Algoritmo de Backpropagation
    def aprender(self, gabarito):
        #para a ultima camada:
        # gabarito: vetor que guarda a saida esperada  
        erro = []
        for i in range(len(gabarito)):
            erro.append((-1)*(gabarito[i] - self.camadas[-1].feedForward()[i]))
        self.camadas[-1].corrigirCamada(erro)
        #para as camadas ocultas e de entrada:
        erro = []
        # itera por todas as camadas da rede de tras para frente
        for c in range(len(self.camadas) - 2, -1, -1):
            # erro = Somatorio das glias * mielina que conecta o neuronio atual com o proximo
            # itera por todos os neuronios dessa camada
            for n in range (len(self.camadas[c].neuronios)):
                erroSing = 0
                # itera por cada neuronio da camada seguinte calculando o fator de erro necessario
                #  para o processo de aprendizado deles.
                for m in range(len(self.camadas[c + 1].neuronios)):
                    erroSing += (self.camadas[c + 1].getGlias()[m] * self.camadas[c + 1].neuronios[m].mielina[n])
                erro.append(erroSing)
            self.camadas[c].corrigirCamada(erro)
        # Atualiza as mielinas das camadas da rede
        for c in self.camadas:
            c.atualizarMielinas()
            
