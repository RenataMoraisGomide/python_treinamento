# Vamos aprender sobre o raise do inglês (elevação) e assert do inglês (afirmar)
# Ambos são comandos específicos do python para levantamento de exceções
# exceções da linguagem python em: docs.python.org/pt-br/3/tutorial/erros.html
# aí você encontrará todos os erros que podemos chamar em raise, aqueles que são usados para algum fim
#Geralmente para desenvolver bibliotecas e usar bibliotecas de terceiros usa-se muito o tratamento de erro
#Ex:


# RAISE
raise ValueError('Deu merda!kkkkk ')        #raise ValueError('Deu merda!kkkkk ')
                                            # ValueError: Deu merda!kkkkk
                                            #podemos usar a exceção que quisermos desde que esteja dentro do doc python

#ex:
def soma(n1, n2):
    return n1 + n2

print(soma(2, 2))                       # Aqui dará certo, 2 e 2 = 4, mais quero que não seja possivel somar                    
                                        # se for um número negativo então fazemos assim:


def soma(n1, n2):
    if n1 < 0 or n2 < 0:                #dizemos então para raise que se n1 ou n2 for < 0 dar um erro chamado ValueError
        raise ValueError('n1 e n2 não podem ser negativos')
    return n1 + n2                      

print(soma(2, -2))

# ASSERT:
# Usamos o assert para afirmar que uma coisa será daquela maneira
# ex:
x = -1
assert x > 0, 'Deu merda! kkkk'
#(Acima falamos que x = -1 e no assert pedimos que ele seja > que 0, então dá erro)
#Se mudarmos o valor inicial de x para > 0 e printa-lo ficará:
x = 2
assert x > 0, 'Deu merda! kkkk'
print(x) #o print será 2