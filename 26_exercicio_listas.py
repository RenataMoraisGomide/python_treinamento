# Receba 10 valores e exiba a soma de todos eles
#Primeiro cria uma variável x que vai receber input de (int), para cada elemento
#  dentro do conjunto receba/ crie uma lista com (10)
#inicia a variavel com o valor = 0 
#para cada i dentro do recebido x faça: soma que recebe a soma(que iniciamos 0) + i (elemento) 
# e print a soma deles


x = [int(input('Digite dez números inteiros: ')) for i in range(0, 10)]
soma = 0
for i in x:
    soma = soma + i   #soma += 1
print(soma)
