# Uma lista pode conter outras litas dentro dela, subdividindo entre linhas e colunas (MATRIZ)
#Uma matriz tem a mesma quantidade de coluna-elementos (se temos 5 números) a próxima tb terá
#Uma lista de lista não precisa ter a mesma quantidade de colunas-elementos
#Exemplo: 

idades = [

            [1,2,3,4,5],        #linha n° 0
            [6,7,8,9,10],       #linha n° 1
            [11,12,13,14,15]    #linha n° 2
]
#Para acessar as linhas e colunas começamos no 0, separados ([n° da linha] [n° da coluna])
#EX:

print(idades[2][4])  #15

# Como fazemos para iterar(percorrer) cada um dos elementos da matriz ou listas de listas?
for i in range(0, len(idades)):
    print(idades[i])        
#Usando o for assim ele trará a lista toda sem separar um a um.       
    ''' [1, 2, 3, 4, 5]     
        [6, 7, 8, 9, 10]    
        [11, 12, 13, 14, 15]'''

#Para iterar um a um (elemento) fazemos:
#O i esta sendo cada linha e o j esta sendo cada objeto da lista
for i in range(0, len(idades)):
    for j in range(0, len(idades[i])):
        print(idades[i][j])










