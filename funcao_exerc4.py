comprimento = 0
largura = 0
altura = 0
volume = 0

def leitura():
    print('Digite o comprimento: ')
    global comprimento
    comprimento = float(input())
    print('Digite a altura: ')
    global largura
    largura = float(input())
    print('Digite o volume: ')
    global altura
    altura = float(input())
    global volume
    volume = comprimento * largura * altura
    print('Volume: ', volume)

leitura()
