# A lambda é uma função que faz parte da programação funcional e que sempre retorna algo mesmo 
# vazio ela retorna none, não precisa usar o return nela pois
# ela já chama o objeto. ela pode receber parâmetros, args *idade (empacota todos os valores que receber dentro de uma tupla)


x = lambda nome, idade: print(f'nome = {nome}\nidade = {idade}')  
x('renata', 20)                 #nome = renata
                                #idade = 20

# Ex. com args:
# definimos uma função teste, chamamos o retorno dela em lambda, falamos para tudo que for colocado dentro de idades
# ser passado para args como tupla
def teste():
    return lambda *idade: print(idade)
x = teste()
print(x)                        #<function teste.<locals>.<lambda> at 0x000001D04D679300>
#dentro desse x posso passar os parâmetros que quero que print:
print('Caio', 'Renata', 'G')            #Caio Renata G

