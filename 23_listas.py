#17/07/23
#Listas: Forma mais compacta para armazenar várias informações em uma única variável
#exemplo:
nomes = ['Caio', 'Renata', 'Rose', 'Georgia', 'Rodrigo']
print(type(nomes))  #tipo list
print(nomes)

#Index é a posição de cada elemento da lista
#O index começa na posição 0 (primeira posição) e é acessado com []
print(nomes [0])
print(nomes [1])
print(nomes [2])
print(nomes [3])
print(nomes [4])

#LEN retorna o tamanho de alguma coisa na lista(quantos nomes por ex.)
print(len(nomes))

#As listas podem ser modificadas(qualquel valor) para qualquer valor
#Vamos trocar o nome do index [2] de Rose por Rosa
nomes[2] = 'Rosa'
print(nomes)

#APPEND é o método que vai adicionar um determinado elemento no final da lista
nomes.append('Clelia')
print(nomes)   #['Caio', 'Renata', 'Rosa', 'Georgia', 'Rodrigo', 'Clelia']

#INSERT é o método que adiciona um elemento em outra posição da lista, você informa para o metodo
#a posição que quer adicional o novo valor e o novo valor:
nomes.insert(0, 'Fabio')    #posição 0 o 'Fabio'
print(nomes)                #['Fabio', 'Caio', 'Renata', 'Rosa', 'Georgia', 'Rodrigo', 'Clelia']
    

#POP: é o método que deleta(remove) o um ítem da sua lista e se rodarmos ele por 2 x por ex.(sem informar qual index)
# ele vai retirando o último. Podemos usar ele informando qual o index queremos que ele delete entre ()
nomes.pop()                 #['Fabio', 'Caio', 'Renata', 'Rosa', 'Georgia', 'Rodrigo']
nomes.pop(2)                #['Fabio', 'Caio', 'Rosa', 'Georgia', 'Rodrigo']
print(nomes)               


#REMOVE: no remove vc informa o valor a ser removido da lista, quando não sabemos a posição de um elemento
# se houver  valores iguais dentro da lista ele remove apenas o primeiro da lista,caso queira remover mais tem
# que dar mais remove
nomes.remove('Fabio')       #['Caio', 'Rosa', 'Georgia', 'Rodrigo']
print(nomes)


#INDEX: é o método que usamos para descobrir a posição do (primeiro) elemento com aquele nome
#  aparece dentro da lista.
print(nomes.index('Georgia'))           # 2


#SORT = método que usamos para ordenar os valores da lista
#pode ser por ordem alfabética, crescente/decrescente.
#usando o .sort(reverse=True) ele trás em ordem decrescente
nomes.sort()                    #['Caio', 'Georgia', 'Rodrigo', 'Rosa']
print(nomes)

#SORTED = é uma função que trás a lista como ela era, retorna uma nova lista copiada
print(sorted(nomes))                #['Caio', 'Georgia', 'Rodrigo', 'Rosa']
                                    #['Caio', 'Georgia', 'Rodrigo', 'Rosa']
print(nomes)







