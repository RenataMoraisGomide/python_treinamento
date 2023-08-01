#Escreva um programa que receba notas de um aluno(0-10), caso a nota esteja fora do intervalo peça ao 
#professor para digita-la novamente

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota < 0 or nota > 10:
        print('Digite a nota válida: ')
        nota = float(input('Digite a nota do aluno: '))
    else:
         print(f'A nota: {nota}, foi registrada com sucesso!')
         break


