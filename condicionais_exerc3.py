print('Digite o numero 1: ')
numero1 = int(input())
print('Digite o numero 2: ')
numero2 = int(input())

if numero1 > numero2:
    print(numero1, 'maior que', numero2)
elif numero2 > numero1:
    print(numero2, 'é maior que ', numero1)
else:
    print('Os numeros são iguais!')
