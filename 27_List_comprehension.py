''' Aqui começaremos a estudar a programação funcional que é a forma de estruturar nosso raciocínio
para chegar em um objetivo, o que muda a forma de estruturar esse raciocínio é o PARADÍGMA DE PROGRAMAÇÃO.
    Existe vários tipos de paradígmas, como por exemplo: orientado a objetos, procedural, funcional etc.
    O Python como já vimos é uma linguagem multiparadigmas podendo ser codificado com vários paradígmas. 
    No python é comum misturarmos os raciocínios.
    Dentro do Paradígma FUNCIONAL temos o List comprehension que é uma forma mais de manipularmos as listas,
fazer comprensão de listas, utilizando uma sintaxe mais curta e direta. 
'''
#EX: list comprehension (programação funcional)
#Essa sintexe significa: Adicione a variável i dentro da lista x, para cada valor da variável i dentro de um
#determinado escopo dentro do for, para cada iteração do for vc adiciona dentro da lista x a varável i.

x = [i for i in range (0, 10)]
print(x)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#fazendo o mesmo exemplo sem programação funcional: (mais longa)
y = []
for i in range(0, 10):
    y.append(i)
print(y)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = [i for i in range(0,10) if i > 4]
print(x)


