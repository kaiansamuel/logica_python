import numpy

TAMANHO = 3
matriz = numpy.empty([TAMANHO, TAMANHO], dtype=numpy.int32)
for linha in  range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        print('Digite o valor da linha ', linha, 'e coluna', coluna, ': ')
        matriz[linha][coluna] = int(input())
print('Digite o valor a ser pesquisado: ')
pesquisa = int(input())

quantidade = 0
for linha in range(0, TAMANHO):
    for coluna in range(0, TAMANHO):
        if matriz[linha][coluna] == pesquisa:
            quantidade += 1

print('Quantidade de numeros encontrados: ', quantidade)