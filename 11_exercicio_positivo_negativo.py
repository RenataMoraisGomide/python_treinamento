#Receba um número e diga se ele é positivo ou negativo


num = float(input('Digite o número: '))

if num > 0:
    print(f'O número {num} é um número positivo')
elif num < 0:
    print(f'O número {num} é um número negativo')
else:
    print(f'O número {num} é um número neutro')

