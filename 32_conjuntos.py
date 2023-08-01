#Listas/dicionários/tuplas/conjuntos
# Conjuntos tem peculariedades que difere das listas e das tuplas apesar de parecidos, os conjuntos não aceitam valores(dados) repetidos
# para criar um conjunto usamos o set()
#ex:


x = [1,1,1,1,2,2,2,4,5,6]           #uma lista normal(pode ter números repetidos etc)
x = set(x)                          #aqui estamos convertendo uma lista x em um conjunto x
print(x)                            #e quando fazemos a conversão o conjunto retira os repetidos ficando: {1, 2, 4, 5, 6} 



x = {1,1,1,2,22,4,3,5,66}           #aqui ele já é um conjunto, então o print tirará os repetidos
print(x)                            #{1, 2, 3, 4, 5, 66, 22}    

# Os conjuntos assim como na matemática temos as uniões .union,
# interseccções .intersection, diferença .difference e diferença simétrica .symetric_difference.
#ex: 

x = {1, 2, 3, 4, 5}
y = {5, 6, 7, 8, 9, 10}
t = x.union(y)              # A .union ira unir os dois conjuntos x e y eliminando os iguais
print(t)                    #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



x = {1, 2, 3, 4, 5}         # A .intersection mostra o que temos repetindo dentro do conjunto, caso não haja 
y = {5, 6, 7, 8, 9, 10}     # valores repetidos ele retorna set() vazio
t = x.intersection(y)
print(t)


x = {1, 2, 3, 4, 5}         # A .difference mostrará os valores que tem em um conjunto que não tem no outro
y = {5, 6, 7, 8, 9, 10}     # no caso aqui os valores que tem em x que não tem em y
t = x.difference(y)
print(t)                    #{1, 2, 3, 4}



x = {1, 2, 3, 4, 5}         
y = {5, 6, 7, 8, 9, 10}         #A diferença simetrica ele somará os elementos do conjunto
t = x.symmetric_difference(y)   # os repetidos saem dos dois conjuntos e os outros permanecem 
print(t)                        #{1, 2, 3, 4, 6, 7, 8, 9, 10} retirou o 5 pois repetiu







