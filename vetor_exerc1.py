import numpy

vetor = numpy.empty(10, dtype=numpy.int32)
for posicao in range(0, 5):
    print('Digite o valor: ', posicao + 1, ':')
    vetor[posicao] = int(input())

print('Digite o valor a ser pesqsuisado: ')
x = int(input())

for posicao in range(0, 5):
    if vetor[posicao] == x:
        print(x, 'foi encontrado ', posicao)
