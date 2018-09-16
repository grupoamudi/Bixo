import NeuronioConvolucional as NC
import random

LARGURA = 128
ALTURA = 256
STRIDE = 1
FILTRO = 8

nc1 = NC.NeuronioConvolucional(
    LARGURA,
    ALTURA,
    STRIDE,
    FILTRO)

# Esperado:
#   Matriz de mielina com FILTRO Colunas
#   Matriz de mielina com FILTRO Linhas
#nc1.printMielina()

# Esperado:
#   Matriz de saida com (LARGURA - FILTRO)/STRIDE Colunas
#   Matriz de saida com (ALTURA - FILTRO)/STRIDE Linhas
#nc1.printAxonio()

# Esperado:
#   FILTRO ao Quadrado
nc1.printTamanhoMielina()

# Esperado:
#   (LARGURA - FILTRO) * (ALTURA - FILTRO) / STRIDE^2
nc1.printTamanhoSaida()

imagemteste = [
                [1, 3, 2, 3, 2, 5],
                [0, 3, 1, 3, 4, 5],
                [1, 0, 0, 3, 3, 5],
                [1, 0, 2, 3, 1, 3],
                [2, 1, 2, 1, 2, 0],
                [1, 3, 2, 3, 2, 5]]

nc1.sinal(imagemteste)

nc1.printDendritos()

imagemteste2 = []
for i in range (128):
    imagemteste2.insert(i,[])
    for j in range (256):
        imagemteste.insert(j,random.random())

nc1.sinal(imagemteste2)

nc1.printAxonio()

nc1.sinapse()

nc1.printAxonio()
