import numpy

nomes = numpy.empty(5, dtype=object)
notas = numpy.empty(5)

for posicao in range(0, 5):
    print('Digite o nome do aluno ', posicao + 1, ': ')
    nomes[posicao] = input()
    print('Digite a nota do aluno ', posicao + 1, ': ')
    notas[posicao] = float(input())

for posicao in range(0, 5):
    print(nomes[posicao], ' - ', notas[posicao])