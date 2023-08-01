# Continuando a programação funcional, temos o MAP
# O MAP nós usamos para aplicar mudanças dentro de uma lista, ele recebe 2 parâmetros também


#EX:

x = [i for i in range(12, 26)]                    #Para cada i dentro de uma lista i faça o range(percorra) list comprehension        
#print(x)                                         #[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#x = list(map(lambda x: 10, x))                   #Usando o MAP aqui todos os valores da lista x passaram a ser 10
x = list(map(lambda x: 10 if x< 18 else(x), x))   #porém isso é meio sem utilidade, então por ex. colocamos condições ifnpor ex. 
print(x)                                          #[10, 10, 10, 10, 10, 10, 18, 19, 20, 21, 22, 23, 24, 25]

