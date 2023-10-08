def calcula_salario():
    valor_bruto = float(input('Digite o seu salário bruto: '))
    adicional_beneficios = float(input('Digite o seu adicional dos benefícios: '))
    if valor_bruto >= 0 and valor_bruto <= 1100:
        valor_imposto = 0.05 * valor_bruto
    elif valor_bruto > 1100 and valor_bruto <= 2500:
        valor_imposto = 0.10 * valor_bruto
    elif valor_bruto > 2500:
        valor_imposto = 0.15 * valor_bruto
    saida = (valor_bruto - valor_imposto) + adicional_beneficios
    print(f'{saida:.2f}')

calcula_salario()