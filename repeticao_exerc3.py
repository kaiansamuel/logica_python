contador = 1
negativos = 0

while contador <= 5:
    print('Digite um valor: ')
    a = float(input())
    if a < 0:
        negativos += 1
    contador += 1

print('Quantidade de numeros negativos: ', negativos)

