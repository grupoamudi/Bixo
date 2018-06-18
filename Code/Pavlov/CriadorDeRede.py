import Rede
import Neuronio
import Camada

def criarRede():
    numeroDeCamadas = int(input("Numero de Camadas: "))
    numeroDeEntradas = int(input("Numero de Entradas: "))
    numeroDeSaidas = int(input("Numero de Saidas: "))

    numeroDeNeuronios = []

    camadasDaRede = []

    for i in range (numeroDeCamadas):
        if i == 0:
            camada = []
            numeroDeNeuronios.append(int(input("Quantos neuronios na camada de entrada?")))
            for j in range (numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeEntradas)
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)

        elif i == numeroDeCamadas-1:
            camada = []
            numeroDeNeuronios.append(numeroDeSaidas)
            for j in range (numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeNeuronios[i-1])
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)

        else:
            camada = []
            numeroDeNeuronios.append(int(input("Quantos neuronios na camada " + str(i+1) + "?")))
            for j in range(numeroDeNeuronios[i]):
                novoNeuronio = Neuronio.Neuronio(numeroDeNeuronios[i-1])
                camada.append(novoNeuronio)
            camadasDaRede.append(camada)

    rede = Rede.Rede(numeroDeCamadas, camadasDaRede)
    return rede
