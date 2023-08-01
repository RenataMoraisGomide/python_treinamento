# Faça um programa que o usuário possa cadastrar n pessoas
# armazenando seu nome, idade, altura

pessoas = []            #criamos uma lista vazia para agregar os valores nela de acordo com o input
while True:             #usamos o while por se tratar de uma questão que não sabemos quantas vezes será usada(quantas cadastros terá)
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
    if decisao == 2:
        break

    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    altura = input('Digite a altura: ')

# Podendo ser feito resumidamente assim:
# pessoa = {'nome': input ('Digite o nome'), 'idade': input('Digite a idade'), 'altura': input('Digite a altura)}

pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
pessoas.append(pessoa)          #o .append faz com que todos os dados de PESSOA sejam jogados dentro da lista pessoas[]
print(pessoas)