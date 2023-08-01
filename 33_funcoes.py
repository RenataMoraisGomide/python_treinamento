# Entendendo as funções:
# Função é uma estrutura que pode ou não receber um valor, processar alguma informação e executar uma 
# determinada ação. Usamos a palavra def. para definir que é uma função e ela acompanha a identação.
# tudo dentro da identação fará parte daquela função. O ideal é dividir o que queremos em várias funções
# DIVIDIR PARA CONQUISTAR
#ex:


def minha_funcao():             # Aqui definimos o que a função irá fazer
    print('Oi')
    print('Tudo bem?')

minha_funcao()                  # Aqui chamamos a função ela irá printar Oi Tudo bem? E podemos chamar ela quantas vezes forem necessária


# ex: quero uma função que irá mostrar a soma dos números de 1 a 100
def minha_funcao():
    soma = 0
    for i in range(0, 101):
        soma += i
    print(soma)         #5050 ( a soma de 0 ate 100 )

minha_funcao()