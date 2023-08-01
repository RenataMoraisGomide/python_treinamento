# Aqui aprendemos a tratar os erros, não deixar o sistema travar, mostrar erro para o usuário etc
# ex: ao tentarmos dividir 2/0 o sistema imprime um erro, chamar uma chave inexistente ele tras erro 
# então começaremos a tentar fazer e não a mandar fazer. Como? Usando o try, tente fazer assim, se não der faça isso


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

try:                                # try do inglês tente, tente fazer assim
    print(n1/n2)

except:                             # except do inglês exceto, se não conseguir try 'nas excessoes' 'erros' faça isso
    print('Não consegui')

finally:                            # finally sempre será executado, seria o final depois de tratar os erros
    print('Finalizei')


# Tratando situações específicas:

try:
    x = int(input('Digite um número: '))
    print(5/x)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0')

finally:
    print('Finalizado')



# Aprendendo a ver qual a exceção que foi capturada, o que aconteceu. 

try:                                        # Nesse ex. estamos passando um try para tentar dividir 5 pelo 
    x = int(input('Digite um número: '))        # input recebido, caso não seja possivel (erro) me mostre o essa exceção 
    print(5/x)                              # qual foi ela? 
except Exception as e:                      # usamos a modularização para usar a exceção como uma variável no caso E
    print(e)                                    # ficando exceto Exceção (que será chamada de e) print o e


# É legal armazenar as exceções dentro de um arquivo de log para sabermos quais os erros estão dando
# como podemos arruma-los etc...








