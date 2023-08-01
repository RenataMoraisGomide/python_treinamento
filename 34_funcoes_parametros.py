# Aqui vamos definir parametros para as funções, dar um argumento para ela
# 

def soma_numeros(n1, n2):       #chamamos a função que irá somar dois números n1 + n2
   print(n1 + n2)               #Printamos eles
                                # Passamos os valores respectivos de n1 e n2(tem que ter ambos e os valores serão respectivos a não ser que seja especificados)
soma_numeros(2,4)               # Damos um valor para a função o n1 e n2 que no caso irá somar 
soma_numeros(4,3)               # passa valer 4
soma_numeros(6,4)               # a mesma função vai trocando o valor pois passamos parametros diferentes
soma_numeros(8,4)     
soma_numeros(9,6)

# Quando queremos receber n valores, não sabemos quantos usamos *args ele receberá os parematros (valores) e colocará em uma tupla
# Podemos colocar (n1, n2, *args) ele coloca os outros números no args
def somar_numeros(*args):
    print(args)
somar_numeros(1,3,5,7)              #(1, 3, 5, 7) TUPLA

# **kwargs = damos nomes para os paramentro e ele empacota dentro de um dicionário.
def somar_numeros(**kwargs):
    print(kwargs)
somar_numeros(teste1 = 1, teste2 = 2, teste3 = 3)       #{'teste1': 1, 'teste2': 2, 'teste3': 3} DICIONÁRIO

#usando o kwargs.get conseguimos verificar se uma função foi passada
def somar_numeros(**kwargs):
    x = kwargs.get('teste2')        # Como teste 2 foi passado lá embaixo então foi passado, caso não tenha sido 
    if x:                               # ele printara none
        print('foi passado')
    else:
        print('não foi passado')   
somar_numeros(teste1 = 1, teste2 = 2, teste3 = 3)      












