print('Digite o tempo da viagem: ')
tempo = float(input())
print('Digite a velocidade média: ')
velocidade = float(input())

distancia = tempo * velocidade
litros = distancia / 12

print('Velocidade média: ', velocidade)
print('Tempo', tempo)
print('Distancia percorrida', distancia)
print('Litros', litros)
