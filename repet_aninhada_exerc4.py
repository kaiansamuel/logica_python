import numpy

matrizA = numpy.empty([3, 3])
matrizB = numpy.empty([3, 3])
matrizC = numpy.empty([3, 3])

TAMANHO = 3

print('Leitura da matriz A')
for linha in range(0, TAMANHO ):
    for coluna in range(0, TAMANHO ):
        print('Digite o valor da linha ', linha, 'e da coluna ', coluna, ': ')
        matrizA[linha][coluna] = int(input())

print('leitura da matriz B')
for linha in range(0, TAMANHO ):
    for coluna in range(0, TAMANHO ):
        print('Digite o valor da linha ', linha, 'e da coluna ', coluna, ': ')
        matrizB[linha][coluna] = int(input())

for linha in range(0, TAMANHO ):
    for coluna in range(0, TAMANHO ):
        matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
        print( matrizC[linha][coluna])