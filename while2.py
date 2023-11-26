contador  = 1
nota = 0
soma = 0

while contador <= 5:
    print('Digite a nota ', contador)
    nota = float(input())
    soma = soma + nota
    contador += 1

print('Total das notas ', soma)
media = soma / 5

if media <= 5.9:
    print('Aluno reprovado!')
else:
    print('Aluno Aprovado!')
print('Media ', media)
