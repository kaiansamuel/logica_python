idade = 0

def leitura(msg):
    print(msg)
    global idade
    idade = int(input())

def faixa(id):
    if id >= 0 and id <= 12:
        print('Criança')
    elif id >= 13 and id <= 17:
        print('Adolescente')
    elif id >= 18:
        print('Adulto')
    else:
        print('Idade Invalida')

leitura("Digite a idade do usuario: ")
faixa(idade)
