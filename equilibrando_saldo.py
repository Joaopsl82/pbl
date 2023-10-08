saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

saldo_atualizado_deposito = saldo_atual + valor_deposito
saldo_atualizado_retirada = saldo_atualizado_deposito - valor_retirada

print(f'Saldo atualizado na conta: {saldo_atualizado_retirada:.1f}')
