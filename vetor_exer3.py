import numpy

A = numpy.empty(10)
B = numpy.empty(10)

for posicao in range(0, 10):
    print('Digite o valor: ', posicao, ': ')
    A[posicao] = float(input())
    B[posicao] = A[posicao] * A[posicao] * A[posicao]

print('Valor A ', A)
print('Valor B ', B)