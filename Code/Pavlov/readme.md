# Projeto Pavlov
O projeto Pavlov é um framework de machine learning produzido para o projeto B1X0 e especificamente criado para a placa Labrador da Caninos Loucos. Inteiramente desenvolvido em python, envolve algoritmos de treinamento e performance.

## Atual Estado
O script de TesteTreino.py está testando a convergência simples dos pesos em um treinamento. Por enquanto se está utilizando um dataset para a porta lógica AND. O atual estado é que ele não está convergindo para tal. Possíveis fontes de problemas:
-> Backpropagation
-> Arquitetura de Rede não adequada

O script do Neuronio foi corrigido e está completamente documentado. Resta agora corrigir o tratamento de treino contido no Camada.py e na Rede.py.

## Estrutura
O usuário define por meio do programa a arquitetura de sua rede. Isso gerará um arquivo de definição de hiperparâmetros de uma rede neural. O programa de treinamento treinará a rede, assim gerando outro arquivo com os pesos treinados que funcionam para as redes que possuem os hiperparâmetros definidos pela rede.
O código possui os seguintes programas por enquanto:

```
├── Pavlov           
    ├── Neuronio.py
    │   └── Atributos
    |   |   └── mielina [f]
    |   |   └── dendritos [f]
    |   |   └── axonio f
    |   |   └── glia [f]
    |   |
    |   └── Métodos
    |       └── sinal([f] : void)
    |       └── sinapse(void : void)
    |       └── produtoEscalar({[f], [f]} : f)
    |       └── logistica(f : f)
    |       └── derivLogistica(f : f)
    |
    ├── <TO-ADD>
    │   └── 

```

## Contribuintes:
```
-> Matheus Comp 
    └── Neurônio
    
-> Vinícius Ariel
    └── Camada
    └── Rede
    
-> Giulia Nardi
    └── Camada
    
-> Alexandre Frederick
    └── Camada
    └── Rede
    
-> Lloyd Rodrigues
    └── Camada
    └── Rede
```
