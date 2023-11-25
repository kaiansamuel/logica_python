print('Digite a nota M1: ')
m1 = float(input())
print('Digite a nota M2: ')
m2 = float(input())
print('Digite a nota M3: ')
m3 = float(input())

media = (m1 + m2 + m3) / 3

if media >= 6:
    print('Aluno Aprovado!')
elif media < 4:
    print('Aluno Reprovado!')
elif media <= 4 and media < 6:
    print('Aluno pegou exame!')
    print('Digite a nota do exame: ')
    exame = float(input())
    if exame >= 6:
        print('Aluno Aprovado!')
    else:
        print('Aluno reprovado no exame!')
