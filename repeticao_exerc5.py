continua = 's'

while continua == 's':
    print('Digite o comprimento: ')
    comprimento = float(input())
    print('Digite a largura: ')
    largura = float(input())
    print('Digite a altura: ')
    altura = float(input())

    volume = comprimento * altura * largura

    print('Deseja ler mais valores?(s/n)')
    print('Volume ', volume)

    continua = input()