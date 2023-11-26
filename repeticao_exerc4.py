nota1 = 11
while nota1 > 10 or nota1 < 0:
    print('Digite a primeira nota: ')
    nota1 = float(input())

nota2 = -1
while nota2 > 10 or nota2 < 0:
    print('Digite a primeira nota: ')
    nota2 = float(input())

media = (nota1 + nota2) / 2
print('Media ', media)

