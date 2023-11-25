print('Digite o numero total de prestações: ')
prestacoes = float(input())
print('Digite a quantidade de prestações pagas: ')
numero_prestacoes_pagas = float(input())
print('Digite o valor de cada prestação')
valor_prestacao = float(input())

total_pago = valor_prestacao * numero_prestacoes_pagas
saldo_devedor = valor_prestacao * (numero_prestacoes_pagas - prestacoes)

print('Total pago: ', total_pago)
print('Saldo Devedor: ', saldo_devedor)
