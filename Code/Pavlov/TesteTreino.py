import Rede
import Camada
import Neuronio
import CriadorDeRede
import csv

rede = CriadorDeRede.criarRede()
dataset = []

with open("data_E.csv") as data:
    dados = csv.reader(data)
    for linha in dados:
        linha = [float(i) for i in linha]
        dataset.append(linha)

rede.alimentarRede(dataset[0])
#print (rede.getIndiceResposta())
