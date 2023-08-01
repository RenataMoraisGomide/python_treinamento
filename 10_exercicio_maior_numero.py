#Receba três números e exiba o maior deles

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior número.')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior número.')
else:
    print(f'{num3} é o maior número')

    




    
num1 = int(input('Digite primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
soma = num1 + num2
total = (f'A soma de {num1} + {num2} vai ser igual a: {soma}')
print(total)