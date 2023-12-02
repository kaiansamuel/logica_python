def leitura():
    print('Digite um numero: ')
    return int(input())

def positivo(numero):
    if numero > 0:
        print('O numero é positivo')
    else:
        print('Numero negativo')
numero = leitura()
resultado = positivo(numero)
