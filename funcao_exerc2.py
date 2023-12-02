C = 0
F = 0

def leitura():
    print('Digite a temperatura em graus Celsius: ')
    global C
    C = float(input())
    global F
    F = (9 * C + 160) / 5
    print('Temperatura em F: ', F)

leitura()