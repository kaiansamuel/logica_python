print('Digite um numero: ')
valor = int(input())

if(valor >= 1 and valor <= 9):
    print('O valor esta na faixa permitida!')
elif (valor < 1 or valor > 11):
    print('O valor esta fora da faixa permitida!')
