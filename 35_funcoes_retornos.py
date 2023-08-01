#O que esperamos de todas as funções é o retorno
# Então o que no exercício anterior 34_funcoes_paramentros quando retornamos de uma função apenas o print é 
# inútil, precisamos dar a ela um retorno
# SEMPRE QUE A FUNÇÃO EXECUTA O RETURN O QUE ESTA ABAIXO DELE NÃO SERÁ EXECUTADO! como se fosse break 
# só será executado se for uma coisa útil dentro da função

def soma_valores(n1, n2):
    soma = n1 + n2
    return soma

print(soma_valores(1, 2))                # 3

x = soma_valores(1, 2 + 4)
print(x)                                 # 7

