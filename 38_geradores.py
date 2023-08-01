# Para entendermos o conceito de geradores, temos que entender o gerenciamento de memória da linguagem python
# foi escrita em outra linguagem de programação a C, então o interpretador da linguagem python se chama ctype
# então tudo no final são estruturas em linguagem C e gastam um certo tipo de memória e foram implementadas em 
# linguagem C. 

#Importando a biblioteca asizeof ela mostrará a quantidade de memória que um objeto ocupa
from pympler.asizeof import asizesof
#print(asizeof(1))      # No caso o número 1 (como qualquer inteiro padrão) ocupa 32 bites de memória em python

# Em caso de lista por ex:
# Vamos ocupar o espaço de memória para armazenar a lista, o espaço de armazenar o int 1 e o 2
# Ocupamos aqui um espaço de 136 bits, sendo que a cada número int. dentro de uma lista
# a dif(acrescimo) de 2 passando de 32b p 40
# Essas funções são as que trazem return
# dependendo do caso o número de memória é enorme, desnecessária e demorado.
# print(asizesof([1, 2]))  

# Em python temos a função yield (colheita) ele provê alguma coisa mais armazena apenas o ultimo, economizando espaço
def dobro():
    yield 1
print(next(dobro()))   # Sempre que chamar essa função ele trará (colhe)o número 1









