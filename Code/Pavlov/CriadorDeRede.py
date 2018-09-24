#################################################
# Nome: CriadorDeRede.py                        #
# Projeto: Projeto Pavlov                       #
# Autoria: Grupo aMuDi                          #
# Dependencia: Neuronio.py, Rede.py e Camada.py #
# Status: Concluido                             #
#################################################
import Rede
import Neuronio
import Camada

#Este script guarda uma unica funcao que cria toda a rede em funcao das entradas do usuario.
# criarRede: Em funcao das entradas do usuario, ele cria a rede.
def criarRede():
    numeroDeCamadas = int(input("Numero de Camadas: "))
    numeroDeEntradas = int(input("Numero de Entradas: "))
    numeroDeSaidas = int(input("Numero de Saidas: "))

    numeroDeNeuronios = []

    camadasDaRede = []

    for i in range (numeroDeCamadas):
        # Nesta condicao se pergunta para o usuario quantos neuronios ele deseja de entrada
        ## para a sua rede.
        if i == 0:
            camada = []
            numeroDeNeuronios.append(int(input("Quantos neuronios na camada de entrada?")))
            # Nesta iteracao, se cria e adiciona tantos neuronios para a camada quantos forem
            ## especificadas pelo usuario.
            for j in range (numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeEntradas)
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)
        
        # Nesta condicao nao ha preferencia de usuario. A ultima camada tera tantos neuronios
        ## quanto saidas.
        elif i == numeroDeCamadas-1:
            camada = []
            numeroDeNeuronios.append(numeroDeSaidas)
            # Nesta iteracao, se cria e adiciona tantos neuronios para a camada quantas forem
            ## as saidas.
            for j in range (numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeNeuronios[i-1])
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)

        # Nesta condicao se cria as camadas intermediarias.
        ## quanto saidas. 
        else:
            camada = []
            numeroDeNeuronios.append(int(input("Quantos neuronios na camada " + str(i+1) + "?")))
            # Nesta iteracao, se cria e adiciona tantos neuronios para a camada quantos forem
            ## especificadas pelo usuario.
            for j in range(numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeNeuronios[i-1])
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)

    rede = Rede.Rede(numeroDeCamadas, camadasDaRede, numeroDeEntradas)
    return rede
