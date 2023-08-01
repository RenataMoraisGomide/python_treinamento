import math
salario_por_hora = float(input())
horas_trabalhadas_mes = float(input())


salario_bruto = math.floor(salario_por_hora * horas_trabalhadas_mes)
imposto_renda = math.floor(salario_bruto * 11 / 100)
inss = math.floor(salario_bruto * 8 / 100)
sindicato = math.floor(salario_bruto * 5 / 100)

total_descontos = (imposto_renda + inss + sindicato)
salario_liquido = math.floor(salario_bruto - total_descontos)


print(f'Salario bruto: {salario_bruto}')
print(f'INSS: {inss}')
print(f'SINDICATO: {sindicato}')
print(f'Salario liquido: {salario_liquido}')










