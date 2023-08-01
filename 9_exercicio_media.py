#Receba 4 notas de um aluno e exiba se ele foi aprovado sendo que:
# (nota maior ou igual a 6 aprovado)
# (nota maior ou igual a 4 recuperacao)
# (nota menor que 4 reprovado)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

nota_total = (nota1+nota2+nota3+nota4)
media = (nota_total)/2

print (f'Sua média foi: {media}')
if media >= 6:
    print('Aprovado!')
elif media >= 4:
    print('Recuperação!')
else:
    print('Reprovado!')