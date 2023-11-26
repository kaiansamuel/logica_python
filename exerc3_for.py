negativos = 0

for contador in range(1, 4):
    print('Digite o valor: ', contador)
    valor = float(input())
    if valor < 0:
        negativos += 1
print('Quantidade de numeros negativos: ', negativos)
