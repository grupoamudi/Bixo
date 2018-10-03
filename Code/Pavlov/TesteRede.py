import Rede
import Camada
import Neuronio
import CriadorDeRede

#declaracao de neuronios que farao parte da camada 1
n1 = Neuronio.Neuronio(4)
n2 = Neuronio.Neuronio(4)
n3 = Neuronio.Neuronio(4)
n4 = Neuronio.Neuronio(4)

#declaracao da camada 1
camada1 = [n1,n2,n3,n4]

cmd1 = Camada.Camada(camada1)

#declaracao de neuronios que farao parte da camada 2
n5 = Neuronio.Neuronio(4)
n6 = Neuronio.Neuronio(4)
n7 = Neuronio.Neuronio(4)

#declaracao da camada 2
camada2 = [n5,n6,n7]

#declaracao das entradas que alimentarao a camada 1
entradas = [1,2,3,4]

matriz = [camada1, camada2]

rede = Rede.Rede(2, matriz)

print(rede.camadas)
print(rede.camadas[0].neuronios)
print(rede.camadas[0].neuronios[0].mielina)

#cmd1.alimentarNeuronios(entradas)
#cmd2.alimentarNeuronios(cmd1.feedForward())

#print (cmd1.neuronios[0].dendritos)
#print (cmd1.neuronios[0].axonio)
#print (cmd1.feedForward())
#print (cmd2.feedForward())
