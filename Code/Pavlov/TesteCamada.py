import Camada
import Neuronio

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

cmd2 = Camada.Camada(camada2)

#entradas que serao mandadas para a camada 1
entradas = [1,2,3,4]

cmd1.alimentarNeuronios(entradas) # limenta a camada 1 com as estradas
cmd2.alimentarNeuronios(cmd1.feedForward()) #alimenta a camada 2 com as saidas da camada 1

print (cmd1.neuronios[0].dendritos) #printa as entradas dos neuronios
print (cmd1.neuronios[0].axonio) #printa as saidas dos neuronios
print (cmd1.feedForward())
print (cmd2.feedForward())
