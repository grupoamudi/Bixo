import Rede
import Camada
import Neuronio
import CriadorDeRede
import csv

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
    with open("data_E.csv") as data:
        dados = csv.reader(data)
        for linha in dados:
            linha = [float(i) for i in linha]
            dataset.append(linha)

    for i in range(len(dataset[0]) - rede.entradas):
        respostas.append(0)

rede = CriadorDeRede.criarRede()
dataset = []
respostas = []
epocas = 50



verificarMielina()

inicializarTreino()

for k in range(epocas):
    for i in dataset:
        for j in range(len(respostas)):
            respostas[j] = i[rede.entradas + j]
        rede.alimentarRede(i)
        rede.aprender(respostas)

verificarMielina()

a = [0,0]
b = [0,1]
c = [1,0]
d = [1,1]

rede.alimentarRede(a)
if (rede.camadas[-1].feedForward()[0] > rede.camadas[-1].feedForward()[1]):
    print("Se Falso e Falso, então: Verdadeiro")
else:
    print("Se Falso e Falso, então: Falso")
    
rede.alimentarRede(b)
if (rede.camadas[-1].feedForward()[0] > rede.camadas[-1].feedForward()[1]):
    print("Se Falso e Verdadeiro, então: Verdadeiro")
else:
    print("Se Falso e Verdadeiro, então: Falso")
    
rede.alimentarRede(c)
if (rede.camadas[-1].feedForward()[0] > rede.camadas[-1].feedForward()[1]):
    print("Se Verdadeiro e Falso, então: Verdadeiro")
else:
    print("Se Verdadeiro e Falso, então: Falso")
    
rede.alimentarRede(d)
if (rede.camadas[-1].feedForward()[0] > rede.camadas[-1].feedForward()[1]):
    print("Se Verdadeiro e Verdadeiro, então: Verdadeiro")
else:
    print("Se Verdadeiro e Verdadeiro, então: Falso")
    
#print (rede.getIndiceResposta())


