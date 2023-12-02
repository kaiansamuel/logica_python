numero = 0

def leitura(msg):
    global numero
    print(msg)
    numero = int(input())

def positivo(num):
    if num <= 0:
        print('Negativo')
    else:
        print('Positivo')

leitura('Digite o numero: ')
positivo(numero)