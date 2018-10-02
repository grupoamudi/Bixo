#############################################
# Nome: Camada.py                           #
# Projeto: Projeto Pavlov                   #
# Autoria: Grupo aMuDi                      #
# Dependencia: Neuronio.py                  #
# Status: Concluido                         #
#############################################

import Neuronio

# Classe Camada: Responsavel por representar uma camada na Rede.
class Camada:
    #Atributos:
    # 1. neuronios: Representa os neuronios contidos na camada.
    neuronios = []
    # 2. saidasDaCamada: Guarda as saidas dos axonios de cada neuronio.
    ## e.g.: A saida do segundo neuronio da camada esta no saidasDaCamada[1].
    saidasDaCamada = []
    # Fim da Descricao.
    
    #Metodos:
    # 1. __init__ : Preenche a camada criada com o numero de neuronios
    ## especificados na entrada da funcao com pesos aleatorios. (Construtor)
    def __init__(self, neuroniosInput):
        self.neuronios = neuroniosInput
        self.saidasDaCamada = [0 for i in range(len(self.neuronios))]
    ### Fim da descricao.
        
    # 2. updateSaidas: Preenche os registros do vetor saidasDaCamada com
    ## as saidas de cada neuronio.
    def updateSaidas (self):
        for i in range(len(self.neuronios)):
            self.saidasDaCamada[i] = self.neuronios[i].axonio
    ### Fim da descricao.   
    
    # 3. alimentarNeuronios: Atualiza as entradas de cada neuronio desta camada
    ## com um vetor de entradas especificado.
    def alimentarNeuronios (self, entradas):
        for neuronio in self.neuronios:
            neuronio.dendritos = entradas
            neuronio.sinapse()
    ### Fim da descricao.

    # 4. feedForward: Atualiza os registros da saida desta camada e retorna esse vetor.
    def feedForward (self):
        self.updateSaidas()
        return self.saidasDaCamada
    ### Fim da descricao.
    
    # 5. corrigirCamada: Dado um vetor indicando o quanto cada neuronio errou, se aciona
    ## os mecanismos de correcao de cada neuronio desta camada com os seus respectivos erros.
    def corrigirCamada(self, erro):
        for n in range(len(self.neuronios)):
            self.neuronios[n].corrigirNeuronio(erro[n])
    ### Fim da descricao.

    # 6. getGlias: Funcao da camada que retorna um vetor com os gradientes descendentes de
    ## de cada neuronio.
    def getGlias(self):
        glias = []
        for i in self.neuronios:
            glias.append(i.glia)
        return glias
    ### Fim da descricao.

    # 7. atualizarMielinas: Depois que a camada ja aciona os mecanismos de correcao dos neuronios,
    ## esta funcao efetiva o aprendizado ao atualizar os pesos/mielina do neuronio.
    def atualizarMielinas(self):
        for n in range(len(self.neuronios)):
            self.neuronios[n].atualizarMielinas()
    ### Fim da descricao.
