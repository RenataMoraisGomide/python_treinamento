#Receba uma temperatura em farenheit e exiba em graus celsius.
#C = 5 * F - 32/9

temperatura_farenheit = float(input('Digite a temperatura em F: '))

temperatura_celsius = 5 * ((temperatura_farenheit - 32) /9)

print(f'A temperatura em Celsius é de: {temperatura_celsius}')