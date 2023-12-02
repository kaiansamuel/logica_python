'''def mensagem(msg, vezes):
    for contador in range(0, vezes):
        print(msg)

mensagem('Hello World', 6)'''

valor1 = 0
valor2 = 0
soma = 0

def leitura():
    global valor1
    valor1 = float(input('Digite o Primeiro valor: '))
    global valor2
    valor2 = float(input('Digite o segundo valor: '))

def soma(val1, val2):
    global soma
    soma = val1 + val2
    print('Soma ', soma)

leitura()
soma(valor1, valor2)
