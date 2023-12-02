tempo = 0
velocidade = 0
distancia = 0
litros = 0

def leitura():
    global tempo
    tempo = int(input('Digite o tempo da viagem: '))
    global velocidade
    velocidade = float(input('Digite a velocidade média: '))
    global distancia
    distancia = tempo * velocidade
    global litros
    litros = distancia / 12

    print('Tempo ', tempo)
    print('Velocidade ', velocidade)
    print('Distancia ', distancia)
    print('Litros ', litros)

leitura()