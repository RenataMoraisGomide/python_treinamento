#Receba o sexo da pessoa e exiba 

sexo = str(input('Qual o seu sexo? M ou F: ')).upper()

if sexo == 'F':
    print('Sexo feminino')
elif sexo == 'M':
    print('Sexo masculino')
else:
    print('Opção inválida')

