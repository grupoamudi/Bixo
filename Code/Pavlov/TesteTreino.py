import Rede
import Camada
import Neuronio
import CriadorDeRede
import csv

def verificarDesempenho(i, dataset, rede):
    rede.alimentarRede(dataset[i])
    print(rede.camadas[-1].feedForward())

def verificarDesempenhoOU(): #aprender o conceito de OU
    a = [0,0] 
    b = [0,1]
    c = [1,0]
    d = [1,1]

    rede.alimentarRede(a) #alimenta a rede com a = [0,0], siginificando Falso ou Falso
    if (rede.camadas[-1].feedForward()[0] > 0.5): #se o valor obtido for maior que 0.5, sera verdadeiro
        print("Se Falso ou Falso, então: Verdadeiro")
    else:
        print("Se Falso ou Falso, então: Falso")

    print(rede.camadas[-1].feedForward()) #printa a resposta obtida
    
    rede.alimentarRede(b) #alimenta a rede com b = [0,1], siginificando Falso ou Verdadeiro
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Falso ou Verdadeiro, então: Verdadeiro")
    else:
        print("Se Falso ou Verdadeiro, então: Falso")

    print(rede.camadas[-1].feedForward())
    
    rede.alimentarRede(c) #alimenta a rede com c = [1,0], siginificando Verdadeiro ou Falso
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Verdadeiro ou Falso, então: Verdadeiro")
    else:
        print("Se Verdadeiro ou Falso, então: Falso")

    print(rede.camadas[-1].feedForward())
    
    rede.alimentarRede(d) #alimenta a rede com d = [1,1], siginificando Verdadeiro ou Verdadeiro
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Verdadeiro ou Verdadeiro, então: Verdadeiro")
    else:
        print("Se Verdadeiro ou Verdadeiro, então: Falso")

    print(rede.camadas[-1].feedForward())

def verificarDesempenhoE(): #aprender o conceito de E
    a = [0,0]
    b = [0,1]
    c = [1,0]
    d = [1,1]

    rede.alimentarRede(a) #alimenta a rede com a = [0,0], siginificando Falso e Falso
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Falso e Falso, então: Verdadeiro")
    else:
        print("Se Falso e Falso, então: Falso")

    print(rede.camadas[-1].feedForward())
    
    rede.alimentarRede(b) #alimenta a rede com b = [0,1], siginificando Falso e Verdadeiro
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Falso e Verdadeiro, então: Verdadeiro")
    else:
        print("Se Falso e Verdadeiro, então: Falso")

    print(rede.camadas[-1].feedForward())
    
    rede.alimentarRede(c) #alimenta a rede com c = [1,0], siginificando Verdadeiro e Falso
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Verdadeiro e Falso, então: Verdadeiro")
    else:
        print("Se Verdadeiro e Falso, então: Falso")

    print(rede.camadas[-1].feedForward())
    
    rede.alimentarRede(d) #alimenta a rede com d = [1,1], siginificando Verdadeiro e Veraddeiro
    if (rede.camadas[-1].feedForward()[0] > 0.5):
        print("Se Verdadeiro e Verdadeiro, então: Verdadeiro")
    else:
        print("Se Verdadeiro e Verdadeiro, então: Falso")

    print(rede.camadas[-1].feedForward())

def verificarRede():
    for i in rede.camadas:
        print("Camada: {}".format(rede.camadas.index(i)))
        for j in i.neuronios:
            print ("\tNeuronio: {}".format(i.neuronios.index(j)))
            print ("\t\tTamanho Mielina: {}".format(len(j.mielina)))

def verificarMielina():
    print("\n\n")
    print("Verificando...")
    for i in rede.camadas:
        print("Camada: {}".format(rede.camadas.index(i)))
        for j in i.neuronios:
            print ("\tNeuronio: {}".format(i.neuronios.index(j)))
            for k in j.mielina:
                print("\t\tMielina {}: ".format(j.mielina.index(k)) + str(k))

def inicializarTreino():
    with open("DataIRIS.csv") as data:
        dados = csv.reader(data)
        for linha in dados:
            linha = [float(i) for i in linha]
            dataset.append(linha)

    for i in range(len(dataset[0]) - rede.entradas):
        respostas.append(0)

rede = CriadorDeRede.criarRede()
dataset = []
respostas = []
epocas = 500



verificarMielina()

#verificarDesempenhoE()

inicializarTreino()

for k in range(epocas):
    for i in dataset:
        for j in range(len(respostas)):
            respostas[j] = i[rede.entradas + j]
        rede.alimentarRede(i)
        rede.aprender(respostas)

verificarMielina()

#verificarDesempenhoE()

verificarDesempenho(0, dataset, rede)
verificarDesempenho(1, dataset, rede)
verificarDesempenho(2, dataset, rede)

#verificarDesempenhoOU()
    
#print (rede.getIndiceResposta())


