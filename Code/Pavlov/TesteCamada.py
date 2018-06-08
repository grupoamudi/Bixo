import Camada
import Neuronio

n1 = Neuronio.Neuronio(4)
n2 = Neuronio.Neuronio(4)
n3 = Neuronio.Neuronio(4)
n4 = Neuronio.Neuronio(4)

camada1 = [n1,n2,n3,n4]

cmd1 = Camada.Camada(camada1)

n5 = Neuronio.Neuronio(4)
n6 = Neuronio.Neuronio(4)
n7 = Neuronio.Neuronio(4)

camada2 = [n5,n6,n7]

cmd2 = Camada.Camada(camada2)

entradas = [1,2,3,4]

cmd1.alimentarNeuronios(entradas)
cmd2.alimentarNeuronios(cmd1.feedForward())

print (cmd1.neuronios[0].dendritos)
print (cmd1.neuronios[0].axonio)
print (cmd1.feedForward())
print (cmd2.feedForward())
