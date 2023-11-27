import numpy

vetor = numpy.empty(5)

vetor[0] = 10
vetor[1] = 5
vetor[2] = 7
vetor[3] = 9
vetor[4] = 21

print(vetor)

for elemento in range(0, 5):
    print(vetor[elemento])
    